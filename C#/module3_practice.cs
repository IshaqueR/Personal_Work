// Basic string formatting

// escape sequences
// escape sequences use a backslash followed by the escape sequence character
// there are a bunch, here are a few: \n is a newline character, \t is a tab character

Console.WriteLine("1Hello\nWorld!");
Console.WriteLine("2Hello\tWorld!");

// There are many kinds of escape sequences, I cannot cover them all here.


// Verbatim string literals
// Uses the @ directive
// Everything is kept as is, i.e. it is kept verbatim, after the directive.

Console.WriteLine(@"    c:\source\repos    
        (this is where your code goes)


 1                   5, 3, 1,                ----> Lets go ");

// Unicode escape characters
// Allows special characters using \u followed by 4-character code of a unicode character.

// Kon'nichiwa World
Console.WriteLine("\u3053\u3093\u306B\u3061\u306F World!");

// Some consoles do not support UTF 16, so if this output just shows question marks,
// it might be a good idea to look into a different console or a different UTF version.


// Combine strings using concatenation
// Concatenation uses the + symbol:
string myName = "Ishaque";
Console.WriteLine("Hello " + myName + "!");

// Combine strings using string interpolation
// Uses curly braces {} and a $ prefixed to the string
Console.WriteLine($"Hello {myName}!");

// Combine verbatim and interpolation:
// Both methods can be combined using $@ (order matters)
string projectName = "First-Project";
Console.WriteLine($@"C:\Output\{projectName}\Data");

// In future I would recommend sticking to interpolation,
// it is cleaner and not difficult to apply.

