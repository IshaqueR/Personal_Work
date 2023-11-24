// number operations

// performing addition with implicit data conversion
// use the + operator for addition

int firstNumber = 12;
int secondNumber = 7;
Console.WriteLine(firstNumber + secondNumber);

// If you mix strings and numbers the compiler will use concatenation
// Therefore it is best to be explicit when coding

Console.WriteLine("12"+secondNumber);

// Other mathematical operations
// Basic mathematical operations include addition, subtraction, multiplication, and division
// Uses +, -, *, and / respectively

int sum = 7 + 5;
int difference = 7 - 5;
int product = 7 * 5;
int quotient = 7 / 5;

Console.WriteLine("Sum: " + sum);
Console.WriteLine("Difference: " + difference);
Console.WriteLine("Product: " + product);
Console.WriteLine("Quotient: " + quotient);

// Division with decimal data
// When you divide two integers and the result data type is an integer the result will be an integer
// To have decimal points, the data type should be decimal, and one of the dividing numbers as well

decimal decimalQuotient = 7.0m / 5;
Console.WriteLine($"Decimal quotient: {decimalQuotient}");

// Data type casting
// This is temporary conversion to a certain data type
// Lets say that you have an int, but you want to do division, so you need a decimal
// You can cast it to a decimal temporarily so that you get a decimal answer

int first = 7;
int second = 5;
decimal answer = (decimal)first / (decimal)second;
Console.WriteLine(answer);

// Determine remainder after integer division
// The modulus operator % returns the remainder of an integer division

Console.WriteLine($"Modulus of 200 / 5 : {200 % 5}");
Console.WriteLine($"Modulus of 7 / 5 : {7 % 5}");

// Increment and Decrement
// This in increasing or decreasing a value
// ++ adds 1, -- subtracts 1
// Also the order matters (before or after value) see the code output:

int value = 1;
value++;
Console.WriteLine("First: " + value);
Console.WriteLine($"Second: {value++}");//done after prints value first then increases
Console.WriteLine("Third: " + value);
Console.WriteLine("Fourth: " + (++value));//done before increases then prints value

// Compund operations
// These are assignment operators combined with math operators to assign the
// value on the right to the value on the left.
// These include +=, -=, *=, /=.

int total = 0;
total += 7; //This is the same as total = total+7, or x = 0+7
total += 5; //This is the same as total = total+5, or x = 7+5

Console.WriteLine(total);