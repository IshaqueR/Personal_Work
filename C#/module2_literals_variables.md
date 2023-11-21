# Learning Path:  [Write your first code using C# (Get started with C#, Part 1)](https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/)

## Module: [Store and retrieve data using literal and variable values in C#](https://learn.microsoft.com/en-us/training/modules/csharp-literals-variables/)

> Before I start here, I just want to note that I have been explaining a bit too much. I will explain only for someone that is already experienced in programming from this point. This is for myself after all. So most of the things will be summarized in point form.

### Unit 1: Introduction

#### Literals
* C# applications will require one to work with data.
* Sometimes the data will be hard-coded into the application.
* Hard-coded values are constant/unchanging in program.
* Correct term for hard-coded values are constants or literal values.

#### Variables
* Most often you work with multiple types of data.
* You can include hard-coded values and user collected information.
* For this you need to define literal values and variables that store a certain type of data.
* Data that is stored in a variable can vary.

#### Learning objectives

* Create literal values for five basic data types.
* Declare and initialize variables.
* Retrieve and set values in variables.
* Allow the compiler to determine the data type for your variable when initializing.

### Unit 2: Print Literal Values

> This unit presents an exercise on printing literal values. On my own I should create a program for practice while following.

#### What is a literal value?
* As discussed before: It's a constant value that **never** changes.
* In the previous module I explicitly printed `Hello World!` in the console. At no point in the programs execution will this value ever change. Meaning: if I run the program over and over again, it will print the same message (unless I change the code).

### Print different literal data types
> There are various data types: strings, integers, etc. I am already familiar with them. This module only looks at 5 types right now. Also side note, this module already covered `strings` as part of the previous module.

#### Character literals
* Characters are single alphanumeric values.
* Placed in single quotes: `'a'` or `'4'` or `'@'`.
* Data type: `char` is short for character.

```csharp
Console.WriteLine('c');
```
#### Integer literals
* Numeric whole numbers (no fractions).
* Does not require extra operators like `string` and `char`.
* Data type: `int` is short for integer.

```csharp
Console.WriteLine(69);
//Yes I'm immature
```

#### Floating-point literals
* Numbers that contain decimals.
* C# supports three data types to represent decimal numbers.
* Data types: `float`, `double`, `decimal`.
* Each type supports varying degrees of precision.

|Float Type | Precision     |
|---------- | ------------  |
|`float`    | ~6-9 digits   |
|`double`   | ~15-17 digits |
|`decimal`  | ~28-29 digits |

##### Float

* To create a float literal, append the letter `F` to the end of the number.
* `F` here is called a literal suffix.
* The casing for literal suffixes does not matter.

```csharp
Console.WriteLine(3.14F);
```

##### Double
* To create a double literal, no suffix is needed.
* Compiler defaults to a double.

```csharp
Console.WriteLine(3.14);
```

##### Decimal
* To create a decimal literal, append the letter `m` to the end of the number.

```csharp
Console.WriteLine(3.14m);
```

#### Boolean literals
* A value consisting of `true` or `false`.
* Data type: `bool` is short for Boolean.
* This data type is important when it comes to decision logic, and evaluating expressions.

```csharp
Console.WriteLine(true);
Console.WriteLine(false);
```

#### Importance of data types
* When you code you essentially work with data.
* Data can be presented, operated on, collected, used in calculation, used in evaluation, stored, etc.
* Programming is essentially working with data.

### Unit 3: Declare variables

* So we established that literals are hard-coded values, they don't change.
* What if you are working with complicated data, like user data, files, etc?
* When you work with data that is not hard-coded, you need a variable.

#### What is a variable?
* A container for storing a type of value.
* Their values can change or **vary** during execution of a program.
* You can assign, read, and change variables.
* Most important is that you can store values in variables that you want to use.
* The compiler assigns variables to locations in memory address.

#### Declare a variable
* A variable needs a data type.
* A variable needs a name or label.

```csharp
string firstName;
```

In the code snippet here, there is a `string` data type variable. The name of the variable is `firstName`. This variable can only hold string values. You can name a variable anything, within syntax rules.

#### Variable name rules and conventions
* Make sure the code is readable and understandable.

> This is a concept that I find strange in some work environments. They do not adhere to clean code conventions and it's just baffling. It makes things much more difficult. Whenever you make code ensure that the person that looks at your code won't be confused and will know what's going on. They should be able to understand with relative ease. Like in the example, the variable `firstName`, it obviously will store a first name of a person. It won't store an age, it won't store a date. That wouldn't make any sense. Be clear when you code.

Some rules for variable names:
* Cannot start with a special character like `$name`, or `!age`. This is invalid.
* Cannot start with a numerical value like `1stDate`, or `3names`. This is invalid.
* They are case sensitive, so `name`, and `Name` are two different variables.
* It cannot be a C# keyword, like `string`. This is a data type, and it is reserved for defining variables as `string` types, therefore it cannot be used as a name.

Some conventions:
* Use **camel case**: start with a small letter, every word that is added onto that first word is started with uppercase. Example: `thisIsCamelCase`.
* Start with alphabetical letter. Underscore is used in certain scenarios but ignore that for now.
* Should be a descriptive name.
* Don't use contractions or abbreviations, it might be unclear what that is. So use full words.
* Don't include the data type of the variable in the name: `strValue`. Don't do this.

##### Here are some examples
```csharp
char userOption;
int gameScore;
decimal particlesPerMillion;
bool processedCustomer;
```

### Unit 4 Setting and getting values from variables.
We covered **declaring** a variable, it requires a data type and a name:
```csharp
string firstName;
```
Next we can **assign** a value to the variable:
```csharp
firstName = "Ishaque";
```
Now the string `Ishaque` is stored in the variable `firstName`. Whenever I use this variable it will use the value stored inside it which is `Ishaque`. Also notice that the data that was assigned it correct, it is indeed a string.

#### Improper assigning
##### Assignment direction
* Assigning happens by assigning the value on the right to the value on the left. Something like this code snippet would be invalid:
```csharp
"Ishaque" = firstName;
```

##### Assignment data type.
* Ensure that the data type that you are working with is the correct data type. The code snippet below is wrong since the data type is an integer (`int`), it is expected to store a number in it, not a string.
```csharp
int firstName;
firstName = "Ishaque";
```

#### Retrieve a value stored in the variable.
After creating and assigning a value to the variable, you can use it in the code. The only method we have used so far is printing a value to the console. So now we will instead print a variable, and not a literal.
```csharp
Console.WriteLine(firstName);
```
The code snippet above is essentially equivalent to:
```csharp
Console.WriteLine("Ishaque");
```
since that is what is stored in the variable. Both will deliver the exact same output: `Ishaque`.

#### Reassignment
You can use the same variable over and over again with different data that it might contain by reassigning a value to it:
```csharp
string firstName
firstName = "Bob";
Console.WriteLine(firstName);
firstName = "Isabella";
Console.WriteLine(firstName);
```
The console will output:
```output
Bob
Isabella
```

> What is happening in the code is, we first create a string variable called `firstName`. The string value `Bob`, is assigned to the variable. We then print the variable to the console (console prints `Bob`). We then change the value inside the variable to `Isabella`. This overwrites whatever was stored inside and reassigns the value to the new value. Now when the variable is printed, the new string value `Isabella` in printed on the console.

#### Possible errors
Sometimes you might forget to assign a value to the variable, and when you use it with a method like `WriteLine()`, you get an error because the variable stores no value. So always keep track of your variables.

### Unit 5 Declare implicitly typed local variables

So far we have looked at explicit declaration of variables, where we specifically assign a data type to the variable. However, you can also infer the variable's data type by the value it is initialized with.

#### What are implicitly typed local variables?

* Created using the `var` keyword, followed by variable initialization.
```csharp
var message = "Hello";
```
In this code snippet, we know that the message - `Hello` - is a `string`, since it is enclosed in double quotes. However, we initialize it with the keyword `var`. The C# compiler will be able to tell what kind of data type it is, similarly like how we did, and **automatically** assign it to that data type. So why do we use `var`? The answer is because we might want to save on keystrokes. If you attempt to reassign the variable message with a different type of data, for instance:
```csharp
message = 12;
```
this will not work as message has now already been defined as a string. So only string reassignments will apply here. Another caveat of the `var` keyword is that the variable has to be initialized upon using the keyword. You can not leave it for later:
```csharp
var message;
```
This declaration above will not work.

#### So why use `var`?
The question arises now, why use this `var` keyword if you can just use the data type instead. The fact is that it is commonly used, and it is important to understand it's use case. Many times, a variable data type is obvious just by looking at it, and for that reason you might want to just use var. It could also assist with coming up with a more dynamic solution. To get used to data types, it is recommended to use them at the beginning.

### Unit 6: Challenge
Practice all the concepts that was learned so far.
> I wrote code in the same folder for this module.

### Unit 7: Review the practice
Like it says, review your practice.

### Unit 8: Knowledge check
Test yourself.

### Unit 9: Summary
Your goal was to display a formatted message using a combination of literal and variable values.

Using basic C# syntax, you created literal values of several different data types. You declared variables, and also set and retrieved values from those variables. You also initialized variables, and learned how to use the `var` keyword to implicitly type a variable by inferring the type from the initialization.

> P.S. this summary was also copied. Man I cannot do these...