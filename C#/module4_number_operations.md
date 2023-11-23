# Learning Path:  [Write your first code using C# (Get started with C#, Part 1)](https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/)

## Module 3: [Perform basic operations on numbers in C#](https://learn.microsoft.com/en-us/training/modules/csharp-basic-operations/)


### Unit 1: Introduction
Applications in C# will consist of literal and variable numeric data. Such as:
* Mathematical operations (addition, subtraction, etc).
* Multi-step operations.
* Remainders after division.
* Increments and decrements.

Learning operators to act on operands like literal and variable values becomes paramount to building an understanding of numeric data applications.

The module teaches how to work with operators and operands correctly so that you can  formulate meaningful instructions.

#### Learning objectives
* Perform mathematical operations on numeric values
* Observe implicit type conversion between strings and numeric values
* Temporarily convert one data type into another


### Unit 2: Perform addition with implicit data conversion
Often you will perform mathematical operations on numeric data. This unit teaches addition and how the compiler parses and interprets your code.

#### Adding two numeric values
* To add two numbers together you use the addition operator `+`.
* It is the same operator used for string concatenation.
* Reusing the symbol for multiple purposes is called **overloading the operator**.
* Compiler will understand what you are trying to do based on the data that is input next to the overloaded operator, i.e. if it is a string, it will perform concatenation, if it is a number, it will perform addition.

The code below shows how addition works:
```csharp
int firstNumber = 12;
int secondNumber = 7;
Console.WriteLine(firstNumber + secondNumber);
```
The output for this will be `19`.

#### Mix data types to force implicit type conversions

If you try to use the `+` symbol with both `string` and `int` values, the compiler will see that the int is surrounded by string values. So it will attempt to implicitly convert the int variable into a string temporarily so that it can concatenate it to the rest of the string. In general the compiler will assist when possible, however ideally you should be explicit about your intentions when coding.

The parentheses symbol is another overloaded operator used for functions as well as for specifying the **order of operations**. It can be used for clarifying the intention when attempting to mix data types.

### Unit 3: Perform math operations
Aside from addition, there are many types of mathematical operations that can be performed.

#### Perform addition, subtraction, multiplication, and division with integers
Observe the following code:
```csharp
int sum = 7 + 5;
int difference = 7 - 5;
int product = 7 * 5;
int quotient = 7 / 5;

Console.WriteLine("Sum: " + sum);
Console.WriteLine("Difference: " + difference);
Console.WriteLine("Product: " + product);
Console.WriteLine("Quotient: " + quotient);
```
The following output will be observed:
```output
Sum: 12
Difference: 2
Product: 35
Quotient: 1
```
From this we can see that:
* `+` is the addition operator.
* `-` is the subtraction operator.
* `*` is the multiplication operator.
* `/` is the division operator.

An important thing to note is that in division, the values after the decimal are truncated from the `quotient` since it is defined as an `int`. Integers cannot have decimals.

#### Performing division using literal decimal data
To use division properly, you should use data that supports fractional digits after the decimal point. So in other words floating-point data types.
```csharp
decimal decimalQuotient = 7.0m / 5;
Console.WriteLine($"Decimal quotient: {decimalQuotient}");
```
In the above code snippet, the output will be:
```output
Decimal quotient: 1.4
```
* For this to work, the variable data type must be specified as decimal. 
* At least one of the dividing numbers must be a decimal.

#### Data type casting
* It is converting data types to other types temporarily.
* The operation is called a **cast**.
* Add the cast operator before the value:
* Use the name of the data type surrounded by parentheses in front of the value.

See the code below:
```csharp
int first = 7;
int second = 5;
decimal quotient = (decimal)first / (decimal)second;
Console.WriteLine(quotient);
```
The above will cast or convert the integers to decimals before performing division.

#### Determine remainder after integer division
* The modulus operator `%` tells you the remainder of an int division.
* This tells you if a number is perfectly divisible by another number.

See the code and output of the remainder (modulus).
```csharp
Console.WriteLine($"Modulus of 200 / 5 : {200 % 5}");
Console.WriteLine($"Modulus of 7 / 5 : {7 % 5}");
```

```output
Modulus of 200 / 5 : 0
Modulus of 7 / 5 : 2
```

#### Order of operations

* As mentioned before, parentheses can be used to denote the order of operations.
* In mathematics there are rules for order of operations, i.e.
1. Parenthesis
2. Exponents
3. Multiplication and Division
4. Addition and subtraction

> System,Math.Pow method can be used for exponents as there is no exponent operators in C#.

### Unit 4: Increment and decrement values

#### Increment and decrement
* Increment is increase.
* Decrement is decrease.
* Use += operator to add and assign the value on the right to the value on the left.
* Use ++ operator to increment the value of a variable by 1.
* Similar things can be done with other mathematical operators.

> Operators like `+=`, `-=`, `*=`, `++`, and `--` are known as **compound assignment operators** because they compound some operation in addition to assigning the result to the variable. The `+=` operator is specifically termed the **addition assignment operator**.

#### Position the increment/decrement operators
The positioning of the increment and decrement operators matter when using it.
* If used before a value it will increment/decrement first and then display the output.
* If used after a value, it will retrieve the value stored in the variable first, and then perform the increment/decrement operation.

See the code below with the use of positioning:
```csharp
int value = 1;
value++;
Console.WriteLine("First: " + value);
Console.WriteLine($"Second: {value++}");
Console.WriteLine("Third: " + value);
Console.WriteLine("Fourth: " + (++value));
```
Output:
```output
First: 2
Second: 2
Third: 3
Fourth: 4
```
> Unit 5: Challenge yourself

> Unit 6: Review the work

> Unit 7: Knowledge check

### Unit 8: Summary
Your goal was to perform basic operations on string and numeric data. As a coding challenge, you converted a value from one unit of measure (Fahrenheit) to another (Celsius) and displayed the result in a formatted message.

You used various operators to perform basic string and mathematical operations. You learned how some symbols are reused (overloaded) as different operators, depending on the context. You learned how the data types of the operands influence the meaning of the operators. Finally, you learned how to change the data type of a value using the cast operator.