# Learning Path:  [Write your first code using C# (Get started with C#, Part 1)](https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/)

## Module 3: [Perform basic string formatting](https://learn.microsoft.com/en-us/training/modules/csharp-basic-formatting/)
> I noticed from the previous notes that the last few units are just testing yourself units. So I'm just going to put down the unit names and not put any data underneath those units. It's a lot of extra work that is not really necessary. Instead I will just make my code as practice like usual and upload to GitHub. I will however still copy the summaries, and I will add the units with no information as a note.

### Unit 1: Introduction
* You can combine and format literal and variable data to create new values.
* C# provides ways to accomplish this.
* This is done by using escape sequences, concatenating strings, and using string interpolation.

#### Learning objectives
* Create string data containing tabs, new lines, and other special characters.
* Create string data containing Unicode characters
* Combine string data into a new string value via concatenation
* Combine string data into a new string value via interpolation

### Unit 2: Combine strings using character escape sequences

#### Format literal strings in C#
This unit will handle different techniques to display special characters, and add different types of formatting to the output.

#### Character escape sequences.
* An **escape character sequence** is an instruction to the run-time to insert a special character that will affect the output of the string.
* They begin with a backslash `\`.
* Followed by the character you're escaping.
* Example `\n` is the new line escape sequence, `\t` is a tab escape sequence.

The below code snippet is an example of how you would use escape sequence characters in code:
```csharp
Console.WriteLine("Hello\nWorld!");
Console.WriteLine("Hello\tWorld!");
```
The output would be something like this:
```output
Hello
World!
Hello   World!
```
As seen in the output terminal, the first line of code simply adds a **newline** between `Hello` and `World!`. The second output displays a tab space being inserted between the string.

There are many other things that you can include in the text with the help of the backslash character. So if you want to add a double quote, which would otherwise confuse the compiler since a string is enclosed in double quotes, you can just add a backslash before it and the double quote will be added. There are many escape sequences. [Check online](https://csharpindepth.com/articles/Strings).

#### Verbatim string literal
* Will keep all whitespace and characters without the need to escape the backslash.
* To create a verbatim string, use the `@` directive before the literal string.

See the example code snippet:
```csharp
Console.WriteLine(@"    c:\source\repos
        (this is where your code goes)");
```
Thee output would look like:
```output
c:\source\repos    
        (this is where your code goes)
```
As it can be seen, everything that is input after the verbatim directive will be kept as is. This is a common way to display strings that may otherwise include several special characters, and avoid adding escape sequences for each one.

#### Unicode escape characters
* Encoded characters in literal strings.
* Makes use of the `\u` escape sequence.
* Followed by a four-character code representing some character in Unicode (UTF-16).

> Some consoles do not support Unicode characters, instead it will replace the characters with question marks.

### Unit 3: Combine strings using string concatenation

Sometimes strings contain data from different sources, and also contains different types (string, numeric, etc.). This unit looks into combining values using string concatenation.

#### String concatenation
* Concatenation is to combine.
* String concatenation is combining strings.
* Not the same as math addition, things are not added, they are joined.

#### Concatenate a literal string and a variable
* To concatenate simply use the `string concatenation operator`, the plus symbol `+`.

Observe the following code:
```csharp
string firstName = "Bob";
string message = "Hello " + firstName;
Console.WriteLine(message);
```
and the output:
```output
Hello Bob
```
Notice that instead of using two different `Write` methods, we can use a single `WriteLine` method and the operator `+` to display all values in a single string.

This can be done for a number of strings and variables, just reuse the `+` operator whenever you want to join things.

#### Avoid intermediate variables
In the previous snippet, an intermediate variable message was used. In general this should be avoided, as it does not change the result if you were to simply print the contents of the message variable straight to terminal, instead this will take up extra memory (instruction cycles). Unless it is completely necessary to do so, this should be avoided.


### Unit 4: Combine strings using string interpolation
While string concatenation is simple and convenient, string interpolation is growing in popularity in situations used for many string formatted messages.

#### String interpolation
* Combines multiple values into a single literal string by using a "template" and one or more *interpolation expressions*.
* Interpolation expression is used by specifying curly braces `{}`.
* You can put any C# expression that returns a single value inside the braces.
* The literal string becomes a template when it is prefixed with the `$` character.

So instead of writing:
```csharp
string message = greeting + " " + firstName + "!";
```
You can do this:
```csharp
string message = $"{greeting} {firstName}!";
```
In this way, keystrokes are saved, concise string interpolation is done, and is useful in complex scenarios. It's also cleaner and easier to read.

#### Combine verbatim literals and string interpolation
You can use both the verbatim literal prefix symbol `@` and the string interpolation `$` symbol together.

See the example code:
```csharp
string projectName = "First-Project";
Console.WriteLine($@"C:\Output\{projectName}\Data");
```
and the output:
```output
C:\Output\First-Project\Data
```
Here the `$` symbol allows you to reference the variable inside the braces, while the `@` symbol allows you to use the `\` character.

> Unit 5: Challenge yourself

> Unit 6: Review the work

> Unit 7: Knowledge check

### Unit 8: Summary
Your goal was to write code that formats strings with special characters, such as double quotes, new lines, tabs, and other white space, as well as unicode characters. You also combined strings using two different techniques.

Using character escape sequences, you added special characters in your literal strings by either using special escaping sequences or using verbatim strings. You used simple string concatenation with the + symbol, and upgraded to string interpolation for combining values into a string template.

Without the ability to format your output, you would be severely restricted in what kinds of information you could present to the user. However, now you can provide your users with sophisticated instructions and feedback with a wide variety of formatting, symbols, and languages.