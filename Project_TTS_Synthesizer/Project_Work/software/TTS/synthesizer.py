#imports
import numpy as np
import math
from scipy.signal import resample_poly
from scipy.io.wavfile import write
import simpleaudio as sa

def create_synth(specs=None):
    """
    function to create a synthesizer for a vowel based on parameters.
    A SPEC object can be passed into this function to specify the specs variable
    Synthesizer
    """
    #if no parameters are specified then assign default object
    if specs is None:
        specs = Spec()
    
    #parameters are initialized, create the synthesizer
    synth = Synth()
    # Loop through time-varying specs
    for spec in list(filter(lambda aname: not aname.startswith("_"),dir(specs))):
        if spec == "FF" or spec == "BW":
            synth.specs[spec] = \
                    [getattr(specs, spec)[i] for i in range(specs.FORMANTS)]
        else:
            synth.specs[spec] = getattr(specs, spec)
    synth.construct()
    return(synth)


class Spec(object):
    """
    The parameters are specified according to the limitations of the Klatt
    design document.
    FS: Sampling frequency
    FORMANTS: Number of Formants
    DUR: Duration of the synthesized audio file
    F0: Fundamental frequency
    FF: Formant frequencies frequencies from f1 to f5
    BW: Formant bandwidths from f1 to f5
    AV: Voicing amplitude
    AVS: Quasi-Sinusoidal voicing amplitude
    AH: Aspiration amplitude
    AF: Frictation amplitude
    SW: Cascade(0)/Parrallel(1) Switch
    FGP: Glottal pole resonator freq
    BGP: Glottal pole resonator bandwidth
    FGZ: Glottal zero resonator freq
    BGZ: Glottal zero resonator bandwidth
    FNP: Nasal pole resonator freq
    BNP: Nasal pole resonator bandwidth
    FNZ: Nasal zero resonator freq
    BNZ: Nasal zero resonator bandwidth
    BGS: Glottal resonator 2 bandwidth
    A1 - A5: Amplitudes of parallel formants in Hz
    AN: Nasal formant amplitude in Hz
    """
    def __init__(self, FS=10000, FORMANTS=6, DUR=1, F0=120,
                       FF=[450, 1450, 2450, 3300, 3750, 4900],
                       BW=[50, 70, 110, 250, 200, 1000],
                       AV=60, AVS=0, AH=0, AF=0,
                       SW=0, FGP=0, BGP=100, FGZ=1500, BGZ=6000,
                       FNP=250, BNP=100, FNZ=250, BNZ=100, BGS=200,
                       A1=0, A2=0, A3=0, A4=0, A5=0, A6=0, AN=0, AB=0):
        self.FS = FS
        self.DUR = DUR
        self.FORMANTS = FORMANTS
        self.NUMSAMPLES = round(FS*DUR)
        self.DT = 1/FS
        self.F0 = np.ones(self.NUMSAMPLES)*F0
        self.FF = [np.ones(self.NUMSAMPLES)*FF[i] for i in range(FORMANTS)]
        self.BW = [np.ones(self.NUMSAMPLES)*BW[i] for i in range(FORMANTS)]
        self.AV = np.ones(self.NUMSAMPLES)*AV
        self.AVS = np.ones(self.NUMSAMPLES)*AVS
        self.AH = np.ones(self.NUMSAMPLES)*AH
        self.AF = np.ones(self.NUMSAMPLES)*AF
        self.FNZ = np.ones(self.NUMSAMPLES)*FNZ
        self.SW = np.ones(self.NUMSAMPLES)*SW
        self.FGP = np.ones(self.NUMSAMPLES)*FGP
        self.BGP = np.ones(self.NUMSAMPLES)*BGP
        self.FGZ = np.ones(self.NUMSAMPLES)*FGZ
        self.BGZ = np.ones(self.NUMSAMPLES)*BGZ
        self.FNP = np.ones(self.NUMSAMPLES)*FNP
        self.BNP = np.ones(self.NUMSAMPLES)*BNP
        self.BNZ = np.ones(self.NUMSAMPLES)*BNZ
        self.BGS = np.ones(self.NUMSAMPLES)*BGS
        self.A1 = np.ones(self.NUMSAMPLES)*A1
        self.A2 = np.ones(self.NUMSAMPLES)*A2
        self.A3 = np.ones(self.NUMSAMPLES)*A3
        self.A4 = np.ones(self.NUMSAMPLES)*A4
        self.A5 = np.ones(self.NUMSAMPLES)*A5
        self.A6 = np.ones(self.NUMSAMPLES)*A6
        self.AN = np.ones(self.NUMSAMPLES)*AN
        self.AB = np.ones(self.NUMSAMPLES)*AB
    

class Synth(object):
    """
    A Klatt synthesizer modelled based on the 1980 paper :
    "Software for a Cascade/parallel Formant synthesizer".
    The synthesizer contains an impulse generator as input, a voicing source
    that consists of the glottal resonators and glottal amplitude controls,
    a noise source modelled as a low pass filter, it also has a cascade vocal
    tract with nasal resonators and formant resonators. The parallel vocal
    tract also contains formant resonators and a nasal pole resonator. The
    output contains a radiation characteristic. Refer to documentation for
    diagram implementation.
    """
    def __init__(self):
        """
        Create synthesis parameters dictionary
        """
        spec_list =  ["F0", "AV", "AVS", "AV", "AF", "AH", "FF", "BW",
                      "FGP", "BGP", "FGZ", "BGZ", "BGS", 
                      "FNP", "BNP", "FNZ", "BNZ",
                      "A1","A2", "A3", "A4", "A5", "A6", "AN", "AB",
                      "SW", "NUMSAMPLES", "FS", "DT"]
        self.specs = {spec: None for spec in spec_list}

    def construct(self):
        """
        Function that builds the synthesizer after initializing parameters.
        """
        self.output = np.zeros(self.specs["NUMSAMPLES"])
        self.voice = voice_source(self)
        self.noise = noise_source(self)
        self.cascade = cascade_tract(self)
        self.parallel = parallel_tract(self)
        self.radiation = radiation_mod(self)
        self.output_module = output_mod(self)
        self.voice.connect([self.cascade, self.parallel])
        self.noise.connect([self.cascade, self.parallel])
        self.cascade.connect([self.radiation])
        self.parallel.connect([self.radiation])
        self.radiation.connect([self.output_module])
        #reference variable
        self.sections = [self.voice, self.noise, self.cascade, self.parallel, self.radiation, self.output_module]
        # Combine all features
        for section in self.sections:
            section.combine()

    def run(self):
        """
        runs the synthesizer for the vowel.
        """
        self.output[:] = np.zeros(self.specs["NUMSAMPLES"])
        # Clear inputs and outputs in each feature
        for section in self.sections:
            for feature in section.features:
                feature.clean()
        for section in self.sections:
            section.run()
        self.output[:] = self.output_module.output[:]

    def to_audio(self):
        """
        Conversion from digital signal to format for audio output file
        """
        assert self.specs["FS"] == 10_000
        y = resample_poly(self.output, 8, 5)
        peak = np.max(np.abs(y))
        if peak > 1:
            y = y/peak

        y = np.round(y * 32767).astype(np.int16)
        return y
    
    def to_audio2(self):
        """
        Conversion from digital signal to format for audio output file
        """
        assert self.specs["FS"] == 10_000
        y = resample_poly(self.output, 8, 5)
        peak = np.max(np.abs(y))
        if peak > 1:
            y = y/peak

        y = np.round(y * 16384).astype(np.int16)
        return y

    def play(self):
        """
        plays the output file
        """
        y = self.to_audio()
# =============================================================================
#         print(type(y))
# =============================================================================
        sa.play_buffer(y, num_channels=1, bytes_per_sample=2, sample_rate=16_000)

    def save(self, path):
        """
        stores output audio file
        """
        y = self.to_audio()
        write(path, 16_000, y)

class feature:
    """
    A Klatt synthesizer consists of multiple resonators and other features
    or features like an impulse generator and noise generator. All of these
    features should be configured to have the same functionality to allow
    passing a signal into it and out of it. It should also have generic
    connection capability to other features or features.
    
    synth is a Klatt synthesizer object
    feats is a list containing other features
    input is the input signal and its length is defined by NUMSAMPLES of Synth object
    output is the output signal and its length is defined by NUMSAMPLES of Synth object
    """
    def __init__(self, synth, feats=None):
        self.synth = synth
        if feats is None:
            self.feats = []
        else:
            self.feats = feats
        self.input = np.zeros(self.synth.specs["NUMSAMPLES"])
        self.output = np.zeros(self.synth.specs["NUMSAMPLES"])

    def send(self):
        """
        Sends the signal of the feature to the next feature in the list (feats)
        """
        for feat in self.feats:
            feat.receive(signal=self.output[:])
            
    def receive(self, signal):
        """
        Receives the feature sent from a previous feature.
        """
        self.input[:] = signal[:]

    def connect(self, features):
        """
        Connects a feature with another feature
        Simply appends the features together in a list in order.
        """
        for feat in features:
            self.feats.append(feat)

    def clean(self):
        """
        deletes the input and output signals of a feature.
        NUMSAMPLES is the length of the feature signal as defined by the
        synthesizer parameters.
        """
        self.input = np.zeros(self.synth.specs["NUMSAMPLES"])
        self.output = np.zeros(self.synth.specs["NUMSAMPLES"])

#components, resonator, impulse train generator, buffer, amplifier, mixer,
#first difference component, low-pass filter, normalizer, noise generator,
#switch

class digital_resonator(feature):
    """
    This is a digital resonator, the fundamental building block of the Klatt
    synthesizer. It will accept a resonant frequency and a bandwidth to
    calculate coefficients. from there it will produce a signal from an input
    which will be able to be cascaded or parallelized with other resonators.
    
    the digital resonator is defined as a feature, so it has basic feature
    functionality within the synthesizer object.
    synth is a Klatt synthsizer object with defined parameters
    anti specifies whether the resonator is an anti-resonator or just regular.
    if a resonator is an anti resonator it uses other specifed equations to
    produce a signal of inverted output.
    """
    def __init__(self,synth,anti=False):
        feature.__init__(self, synth)
        self.anti=anti
    
    def constants(self, F, BW):
        """
        Parameters
        ----------
        F : list of resonant frequencies of a formant in Hz
        BW : list of bandwidths of the resonant frequncies for the formant in Hz

        Returns
        -------
        Calculates A, B, and C according to equations developed by Klatt.
        """
        C = -np.exp(-2*np.pi*BW*self.synth.specs["DT"])
        B = (2*np.exp(-np.pi*BW*self.synth.specs["DT"])*np.cos(2*np.pi*F*self.synth.specs["DT"]))
        A = 1-C-B
        if self.anti:
            Ap = 1/A
            Bp = -B/A
            Cp = -C/A
            return(Ap, Bp, Cp)
        else:
            return(A, B, C)
        
    def resonate(self, F, BW):
        """
        Does the whole filtering thing from an input inpulse signal to create
        the correct output signal. Signals can then be connected to other
        resonators or whatever. The diagram is in the paper for the calc.
        It makes use of two buffers and a certain realization. Anti resonators
        are just the opposite calculation with different coefficients.
        """
        A, B, C = self.constants(F, BW)
        self.output[0] = A[0]*self.input[0]
        if self.anti:
            self.output[1] = A[1]*self.input[1] + B[1]*self.input[0]
            for i in range(2, self.synth.specs["NUMSAMPLES"]):
                self.output[i] = A[i]*self.input[i] + B[i]*self.input[i-1] + C[i]*self.input[i-2]
        else:
            self.output[1] = A[1]*self.input[1] + B[1]*self.output[0]
            for i in range(2,self.synth.specs["NUMSAMPLES"]):
                self.output[i] = A[i]*self.input[i] + B[i]*self.output[i-1] + C[i]*self.output[i-2]
        self.send()

class impulse_train_gen(feature):
    """
    Generates pulses according to sample rate/fundamental frequency (from doc)
    Keeps track of the index where the last glottal impulse was generated.
    The sample rate/fundamental frequency is the glottal impulse period.
    """
    def __init__(self, synth):
        feature.__init__(self, synth)
        self.glot_ind = 0

    def impulse_gen(self, F0):
        """
        Function to generate pulses (1s)
        """
        glot_per = np.round(self.synth.specs["FS"]/F0)
        self.glot_ind = 0
        for i in range(self.synth.specs["NUMSAMPLES"]):
            if i - self.glot_ind >= glot_per[i]:
                self.output[i] = 1
                self.glot_ind = i
        self.send()

class buffer(feature):
    """
    Just propogates the signal to other components/features
    """
    def __init__(self, synth, feats=None):
        feature.__init__(self, synth, feats)

    def process(self):
        """
        Sets output to input,then sends output.
        """
        self.output[:] = self.input[:]
        self.send()


class signal_mixer(feature):
    """
    Summer, sums signals to produce new signal
    """
    def __init__(self, synth):
        feature.__init__(self, synth)

    def receive(self, signal):
        """
        mixes the signal upon receiving
        """
        self.input[:] = self.input[:] + signal[:]

    def mix(self):
        """
        Concludes the setting the output to the input mixed signal.
        """
        self.output[:] = self.input[:]
        self.send()


class amplifier(feature):
    """
    Increases amplitude of signal by a given dB spec
    """
    def __init__(self, synth):
        feature.__init__(self, synth)

    def amplify(self, dB):
        dB = np.sqrt(10)**(dB/10)
        self.output[:] = self.input[:]*dB
        self.send()


class firstdiff(feature):
    """
    Does a first difference operation on the input signal according to
    the paper equation.
    """
    def __init__(self, synth):
        feature.__init__(self, synth)

    def difference(self):
        self.output[0] = 0
        for i in range(1, self.synth.specs["NUMSAMPLES"]):
            self.output[i] = self.input[i] - self.input[i-1]
        self.send()


class lowpass_filter(feature):
    """
    A one-zero 6 dB/oct lowpass filter.
    """
    def __init__(self, synth):
        feature.__init__(self, synth)

    def filter(self):
        self.output[0] = self.input[0]
        for i in range(1, self.synth.specs["NUMSAMPLES"]):
            self.output[i] = self.input[i] + self.output[i-1]
        self.send()


class normalizer(feature):
    """
    Normalizes a signal.
    """
    def __init__(self, synth):
        feature.__init__(self, synth)

    def normalize(self):
        self.output[:] = self.input[:]/np.max(np.abs(self.input[:]))
        self.send()


class noise_generator(feature):
    """
    Generates noise using a normal distribution.
    """
    def __init__(self, synth):
        feature.__init__(self, synth)

    def generate(self):
        """
        The mean is 0, and standard deviation is 1 for the distribution
        """
        self.output[:] = np.random.normal(0.0, 1.0, self.synth.specs["NUMSAMPLES"])
        self.send()


class synthesis_switch(feature):
    """
    Switch chooses between cascade or parallel vocal tract outputs. Therefore
    there are two output signals, but only 1 is enabled, it will be stored in
    a single variable.
    """
    def __init__(self, synth):
        feature.__init__(self, synth)
        self.output = []
        self.output.append(np.zeros(self.synth.specs["NUMSAMPLES"]))
        self.output.append(np.zeros(self.synth.specs["NUMSAMPLES"]))

    def send(self):
        """
        different version of the send function, this one sends output signals
        to both vocal tracts.
        """
        self.feats[0].receive(signal=self.output[0][:])
        self.feats[1].receive(signal=self.output[1][:])

    def operate(self, select):
        """
        this implements the switch
        """
        for i in range(self.synth.specs["NUMSAMPLES"]):
            if select[i] == 0:
                self.output[0][i] = self.input[i]
                self.output[1][i] = 0
            elif select[i] == 1:
                self.output[0][i] = 0
                self.output[1][i] = self.input[i]
        self.send()

    def clean(self):
        self.output = []
        self.output.append(np.zeros(self.synth.specs["NUMSAMPLES"]))
        self.output.append(np.zeros(self.synth.specs["NUMSAMPLES"]))
        
#SECTIONS HERE
class section:
    """
    Section is a combination of components or features, the sections include
    the voicing source, noise source, cascade vocal tract, parallel vocal tract,
    radiation, and the output module.
    """
    def __init__(self, synth):
        self.synth = synth
        self.features = []
        self.inputs = []
        self.outputs = []

    def connect(self, sects):
        """
        The connect function but for sections. Signal gets sent through a
        buffer.
        """
        for sect in sects:
            sect.inputs.append(buffer(self.synth))
            self.outputs.append(buffer(self.synth, [sect.inputs[-1]]))

    """
    process calls buffer's process function
    """
    def process_ins(self):
        for ins in self.inputs:
            ins.process()

    def process_outs(self):
        for outs in self.outputs:
            outs.process()

    def run(self):
        if self.inputs is not None:
            self.process_ins()
        self.do()
        if self.outputs is not None:
            self.process_outs()
            

class voice_source(section):
    """
    consists of impulse, 2 resonators, 1 anti resonator, 2 amplifiers, a mixer
    and finally into a switch. 
    """
    def __init__(self, synth):
        section.__init__(self, synth)
        self.impulse = impulse_train_gen(self.synth)
        self.rgp = digital_resonator(self.synth)
        self.rgz = digital_resonator(self.synth, anti=True)
        self.rgs = digital_resonator(self.synth)
        self.av = amplifier(self.synth)
        self.avs = amplifier(self.synth)
        self.mixer = signal_mixer(self.synth)
        self.switch = synthesis_switch(self.synth)
        self.components = [self.impulse, self.rgp, self.rgz, self.rgs, \
                           self.av, self.avs, self.mixer, self.switch]

    def combine(self):
        self.impulse.connect([self.rgp])
        self.rgp.connect([self.rgz, self.rgs])
        self.rgz.connect([self.av])
        self.rgs.connect([self.avs])
        self.av.connect([self.mixer])
        self.avs.connect([self.mixer])
        self.mixer.connect([self.switch])
        self.switch.connect([*self.outputs])

    def do(self):
        self.impulse.impulse_gen(self.synth.specs["F0"])
        self.rgp.resonate(self.synth.specs["FGP"],self.synth.specs["BGP"])
        self.rgz.resonate(self.synth.specs["FGZ"],self.synth.specs["BGZ"])
        self.rgs.resonate(self.synth.specs["FGP"],self.synth.specs["BGS"])
        self.av.amplify(self.synth.specs["AV"])
        self.avs.amplify(self.synth.specs["AVS"])
        self.mixer.mix()
        self.switch.operate(self.synth.specs["SW"])


class noise_source(section):
    """
    Guassian noise source
    """
    def __init__(self, synth):
        section.__init__(self, synth)
        self.noisegen = noise_generator(self.synth)
        self.lowpass = lowpass_filter(self.synth)
        self.amp = amplifier(self.synth)
        self.components = [self.noisegen, self.lowpass, self.amp]

    def combine(self):
        self.noisegen.connect([self.lowpass])
        self.lowpass.connect([self.amp])
        self.amp.connect([*self.outputs])

    def do(self):
        self.noisegen.generate()
        self.lowpass.filter()
        self.amp.amplify(-60)


class cascade_tract(section):
    """
    Creates a cascade vocal tract section by combining components.
    """
    def __init__(self, synth):
        section.__init__(self, synth)
        self.ah = amplifier(self.synth)
        self.mixer = signal_mixer(self.synth)
        self.rnp = digital_resonator(self.synth)
        self.rnz = digital_resonator(self.synth, anti=True)
        self.formants = []
        for i in range(self.synth.specs["FORMANTS"]):
            self.formants.append(digital_resonator(self.synth))
        self.components = [self.ah, self.mixer, self.rnp, self.rnz] + self.formants

    def combine(self):
        self.inputs[0].connect([self.mixer])
        self.inputs[1].connect([self.ah])
        self.ah.connect([self.mixer])
        self.mixer.connect([self.rnp])
        self.rnp.connect([self.rnz])
        self.rnz.connect([self.formants[0]])
        for i in range(0, self.synth.specs["FORMANTS"]-1):
            self.formants[i].connect([self.formants[i+1]])
        self.formants[self.synth.specs["FORMANTS"]-1].connect([*self.outputs])

    def do(self):
        self.ah.amplify(self.synth.specs["AH"])
        self.mixer.mix()
        self.rnp.resonate(self.synth.specs["FNP"], self.synth.specs["BNP"])
        self.rnz.resonate(self.synth.specs["FNZ"], self.synth.specs["BNZ"])
        for i in range(len(self.formants)):
            self.formants[i].resonate(self.synth.specs["FF"][i], self.synth.specs["BW"][i])


class parallel_tract(section):
    """
    Creates a parallel vocal tract section
    """
    def __init__(self, synth):
        section.__init__(self, synth)
        self.af = amplifier(self.synth)
        self.a1 = amplifier(self.synth)
        self.r1 = digital_resonator(self.synth)
        self.first_diff = firstdiff(self.synth)
        self.mixer = signal_mixer(self.synth)
        self.an = amplifier(self.synth)
        self.rnp = digital_resonator(self.synth)
        self.a2 = amplifier(self.synth)
        self.r2 = digital_resonator(self.synth)
        self.a3 = amplifier(self.synth)
        self.r3 = digital_resonator(self.synth)
        self.a4 = amplifier(self.synth)
        self.r4 = digital_resonator(self.synth)
        self.a5 = amplifier(self.synth)
        self.r5 = digital_resonator(self.synth)
        self.a6 = amplifier(self.synth)
        self.r6 = digital_resonator(self.synth)
        self.ab = amplifier(self.synth)
        self.output_mixer = signal_mixer(synth=self.synth)
        self.components = [self.af, self.a1, self.r1, self.first_diff,
                           self.mixer, self.an, self.rnp, self.a2, self.r2,
                           self.r1, self.first_diff, self.mixer, self.an,
                           self.rnp, self.a2, self.r2, self.a3, self.r3,
                           self.a4, self.r4, self.a5, self.r5, self.a6,
                           self.r6, self.ab, self.output_mixer]

    def combine(self):
        self.inputs[1].connect([self.af])
        self.inputs[0].connect([self.a1, self.first_diff])
        self.af.connect([self.mixer, self.a5, self.a6, self.ab])
        self.first_diff.connect([self.mixer])
        self.mixer.connect([self.an, self.a2, self.a3, self.a4])
        self.a1.connect([self.r1])
        self.an.connect([self.rnp])
        self.a2.connect([self.r2])
        self.a3.connect([self.r3])
        self.a4.connect([self.r4])
        self.a5.connect([self.r5])
        self.a6.connect([self.r6])
        for comp in [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.rnp, self.ab]:
            comp.connect([self.output_mixer])
        self.output_mixer.connect([*self.outputs])

    def do(self):
        self.af.amplify(self.synth.specs["AF"])
        self.a1.amplify(self.synth.specs["A1"])
        self.r1.resonate(self.synth.specs["FF"][0],self.synth.specs["BW"][0])
        self.first_diff.difference()
        self.mixer.mix()
        self.an.amplify(self.synth.specs["AN"])
        self.rnp.resonate(self.synth.specs["FNP"],self.synth.specs["BNP"])
        self.a2.amplify(self.synth.specs["A2"])
        self.r2.resonate(self.synth.specs["FF"][1],self.synth.specs["BW"][1])
        self.a3.amplify(self.synth.specs["A3"])
        self.r3.resonate(self.synth.specs["FF"][2],self.synth.specs["BW"][2])
        self.a4.amplify(self.synth.specs["A4"])
        self.r4.resonate(self.synth.specs["FF"][3],self.synth.specs["BW"][3])
        self.a5.amplify(self.synth.specs["A5"])
        self.r5.resonate(self.synth.specs["FF"][4],self.synth.specs["BW"][4])
        self.a6.amplify(self.synth.specs["A6"])
        self.r6.resonate(self.synth.specs["FF"][5],self.synth.specs["BW"][5])
        self.ab.amplify(self.synth.specs["AB"])
        self.output_mixer.mix()


class radiation_mod(section):
    """
    Simulates radiation characteristic from the lips
    """
    def __init__(self, synth):
        section.__init__(self, synth)
        self.mixer = signal_mixer(self.synth)
        self.first_diff = firstdiff(self.synth)
        self.components = [self.mixer, self.first_diff]

    def combine(self):
        for inp in self.inputs:
            inp.connect([self.mixer])
        self.mixer.connect([self.first_diff])
        self.first_diff.connect([*self.outputs])

    def do(self):
        self.mixer.mix()
        self.first_diff.difference()


class output_mod(section):
    """
    Mix and normalize the output waveform
    """
    def __init__(self, synth):
        section.__init__(self, synth)
        self.mixer = signal_mixer(self.synth)
        self.norm = normalizer(self.synth)
        self.output = np.zeros(self.synth.specs["NUMSAMPLES"])
        self.components = [self.mixer, self.norm]

    def combine(self):
        for inp in self.inputs:
            inp.feats = [self.mixer]
        self.mixer.feats = [self.norm]
        self.norm.feats = [*self.outputs]

    def do(self):
        self.mixer.mix()
        self.norm.normalize()
        self.output[:] = self.norm.output[:]

if __name__ == '__main__':
    import pylab as pl
    s = create_synth(Spec(DUR=0.5))
    s.run()
    a = s.noise.outputs[0]
    