# Learning Path:  [Write your first code using C# (Get started with C#, Part 1)](https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/)

## Module: [Write your first C# code](https://learn.microsoft.com/en-us/training/modules/csharp-write-first/)

### Unit 1: Introduction

> **Note:** Before I begin with my notes. I want to clarify that I am using Microsoft resources. The links are provided in the heading names. I try to write notes in a way that I can understand for myself. And most of my notes will only include the very important things. So if they just keep on repeating the same thing over and over again, or if it is common knowledge to me then I might not include it. But I will try my best to include as much as I can. This is just how I took notes in my Lab books when working on practical assignments during my engineering studies. So without further ado, I suppose I can start with my very first GitHub notes. Let's begin.

#### C# types of applications
The first section discusses the capabilities of C# as a programming language in building different types of applications. The application types it mentions are not important but I will list them here regardless:
* Business applications
* Web applications
* Games
* Financial and scientific applications
* Cloud-based applications
* Mobile applications

> So the point that is being driven home here is that C# has many applications.

#### What is an application
An Application: 
* Is code that performs a task.
* Best way to learn code is to *write* code.
* Writing code accelerates learning.

> I actually agree with this, and cannot emphasize enough. Whenever you learn coding, make sure you are coding. Best way to learn is by coding what you are learning.

#### Module summary
The concepts that this module explores is:
* Writing first lines of C# code.
* Use two different techniques to print a message as output.
* Diagnose errors when code is incorrect.
* Identify different C# syntax elements like operators, classes, and methods.

> For the record I have already coded in C# before, just the basics though. I have programmed a lot in my studies (other languages) so I have experience.

By the end of this module, I should be able to print messages to a console (windows terminal). I should grasp an idea of what C# syntax looks like.

> Okay, right off the bat, they are talking about concepts that might seem confusing to beginners. Firstly C# is pronounced **C sharp** (not C hash - please don't say this lol). **Syntax** means the way that something is written, in this case, the way that C# code is written. This means spacing, casing, parenthesis, etc. Code is written in **lines**, that's self explanatory. All content will be explained.

### Unit 2: Exercise - Write your first code

#### Writing to console
Unit 2 starts off with an exercise on printing a phrase to the console. The console is a standard output media.
> I use visual studio to code, but you can use essentially any IDE (integrated development environment) that supports C# to code with. At first I would either recommend watching a video on an installation on an IDE for C# like visual studio, and make sure that the video includes a tutorial on running some very basic code. However, when beginning to learn to code it is okay to use an online IDE. Just search an online C# IDE, that should be enough for this module.

So printing a phrase to the console simply means that you will display some sort of message to the terminal where you can view it. This is the "Hello World!" introduction to coding. For this I am using the online .NET editor and output console. The code snippet below is for printing messages to the console.

```csharp
Console.WriteLine("Hello World!");
```

#### Possible errors
When this runs it outputs on the console: `Hello World!`. If there are errors then it could mean a few things. There are things to take note of when writing C# code:
* The first thing is that the functions are case sensitive. This means that from the code snippet, if Console is written with lowercase 'c', then it would throw an error. WriteLine is another function that is case sensitive.
* The second error might be due to the missing semi-colon ';'. At the end of each function in C#, it is required to produce a semi-colon as a delimiter. Kind of like every sentence needs a punctuation mark at the end for it to make sense to us when we read.
* The other possible error could be due to using single quotation marks (' ') instead of double (" "). In C# double quotation marks are used to represent strings (long texts), while single quotations are used for single characters (like letters of the alphabet).
* In general if you make spelling mistakes in the function names, accidental spaces, etc, then it would also throw an error.

> You can always fix your error when you find it and just rerun the code. To ensure that there are no errors in your code, you can simply copy and paste code to avoid unnecessary mistakes. Although be sure to consider plagiarism when you work on your own code in the future. Always give credit.

The console will display any errors that you might have and from them you might be able to discern what the issue is. Additionally, when coding, the code editor highlights a pre-compilation of errors to help you identify and correct mistakes as you develop code. These are the red or yellow underlines which indicates an error or warning in your code respectively. 

#### Comments
When you just want to make notes for yourself or type in something in your code that will help explain what your code does, you will make use of comments. Comments in C# make use of the two forward slashes `//` before a text. Usually you also do this when you want to ignore lines of code in your file. Below is an example of commented code.

```csharp
// Console.WriteLine("Hello World!");
```

#### Another example
Have a look at the next snippet of code:
```csharp
Console.Write("Congratulations!");
Console.Write(" ");
Console.Write("You wrote your first lines of code.");
```
In this code we use the function Console.Write() instead of Console.WriteLine(). And we are also using the function to print three times. The output for this would be:

`Congratulations! You wrote your first lines of code.`

#### Console.Write vs Console.WriteLine
In the previous example, the difference between the two functions has been highlighted. In `Console.WriteLine` there is a line added at the end of the printed statement. In `Console.Write`, there is no line added, so everything appears directly after each other. To further explore the concept, alternate between `Write` and `WriteLine` with the second example that was used to gain better understanding.

### Unit 3: How it works
> Okay, now I'm getting into the nitty gritty theory. I'm going to summarize a lot from here on out, including in future modules and notes.

To understand how code works, you need to think about what programming is, and how the code communicates to the computer. I won't delve too deep since I know all of this, but I will just highlight important concepts.

#### Programming language
* Programming allows you to write instructions that the computer has to perform. 
* Each language has it's own syntax (structure). Though they are similar in nature.
* When coding, you need to *compile* the code into a *format* that the *computer* will understand.

#### What is compilation?
A compiler converts code into a format that the CPU can recognize. You may be familiar with binary and such concepts (this happens at a lower level). This is called machine language, and when you code with languages made easier for people to work with (C#, C, Python, etc), you are essentially working at a high level. In essence, a computer understands machine language, not C#, a compiler is the converter for your PC.

#### What is syntax?
I already touched on this topic. Syntax is the structure of the code. It is the rules, the keywords, operators, colors, etc. It is essentially everything that distinguishes programming languages from each other.

#### How did the code work?
I won't talk too much about this. Just know that everything in object orientated programming has to do with a hierarchical system. That means that some things contain other things, and they have relationships with each other. I already mentioned the word function. The word function and method can be used interchangeably. Just think of a method as a box with tools inside, and each of those tools do something. Now a Class is like a garage, it contains all the methods that contain all the tools. The dot operator (.) is what we use to access methods that are contained within classes. So in our example, `Console` is a Class. `WriteLine()` and `Write()` are methods of the `Console` Class. And, if we wish to access these methods, we need to use the dot operator. Hence `Console.WriteLine()`. The things that we put inside the parenthesis of the method is what we want the method to work with. So we can give it some numbers, some letters, anything as long as it satisfies the criteria of the method. If this is too confusing it's fine, just know that `Console.WriteLine()` and `Console.Write()` is used to print statements to the console.

#### Order of execution
In C# much like other languages, code is executed one line at a time. This means that line 1 is executed before line 2 and so on. This is called sequential programming.

### Unit 4: Challenge
This unit is a simple exercise using WriteLine and Write.
I suggest practicing on an IDE with your own statements to see if you can do it by yourself.
### Unit 5: Review Challenge
Review the work that you have done. Can you do it in any other ways. The answer is yes, you can experiment with different combinations of the same function.
### Unit 6: Knowledge Check
Review the work in this unit and ensure that all the major points are understood.
### Unit 7: Summary
Your goal was to write code that displayed simple messages to an output console while familiarizing yourself with the syntax. You wrote your first lines of code using basic C# syntax. You learned two techniques for displaying literal-string data to the console. You also learned what to look for when you come across an error in your code. And lastly, you identified C# syntax elements like classes and methods, and the purpose of several special symbols that are known as operators. You've taken your first steps towards building more sophisticated applications.
> **Note:** I took the above paragraph directly from the Microsoft module. Sheesh I'm too lazy, I did a lot today. Don't sue me XD
