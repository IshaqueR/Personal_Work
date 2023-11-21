//Printing Literals

//  1. Strings
//  Strings require double quotes " ". 
Console.WriteLine("Strings");
Console.WriteLine("ABCDEFG");

//  The following line would throw an error.
//  This is due to the single quotes used.
//  Console.WriteLine('A string');

//  2. Characters
//  Characters require single quotes and 1 character.
Console.WriteLine("Characters");
Console.WriteLine('c');

//  The following line would throw an error.
//  This is due to mupltiple characters.
//  Console.WriteLine('ab');

//  3. Integers
//  Whole numbers, no fraction, no decimal
Console.WriteLine("Integers");
Console.WriteLine(69);

//  4. Floating-points
//  There are three types of floating points.
//  These are floats, doubles, and decimals.

//  Floats require suffix letter 'F', casing doesn't matter.
Console.WriteLine("Floats");
Console.WriteLine(3.14F);
Console.WriteLine(3.14f);

//  Doubles require no suffix, it is compiler default.
Console.WriteLine("Doubles");
Console.WriteLine(3.14);

//  Decimals require suffix letter 'm', casing doesn't matter.
Console.WriteLine("Decimals");
Console.WriteLine(3.14m);
Console.WriteLine(3.14M);

//  5. Booleans
//  Important for decision logic.
//  An expression will either evaluate to true or false.
//  Casing matters, should be in lowercase.
Console.WriteLine("Booleans");
Console.WriteLine(true);
Console.WriteLine(false);


//  Variables

//  Declaring variables
//  All variables require a data type, and a name.
//  Use naming conventions and avoid errors when naming variables.
string firstName;

//  More examples:
char userOption;
int gameScore;
decimal particlesPerMillion;
bool processedCustomer;

//  Next a value is assigned to the variable
//  Take note of the rules for variable assignment
firstName = "Ishaque";

//  The variable can then be used in a method like printing:
Console.WriteLine("This is my variable: ");
Console.WriteLine(firstName);

//  You can also reassign variables:
//  Assigning the name Bobby:
firstName = "Bobby";
//  Printing the name Bobby:
Console.WriteLine(firstName);

//  Assigning the name Isabella:
firstName = "Isabella";
//  Printing the name Isabella:
Console.WriteLine(firstName);


//  Implicit variable declaration:
//  var keyword can be used to create any type of variable:
//  Implying a string data type:
var myName = "Jimmy";
Console.WriteLine(myName);

//  Implying an int data type:
var myAge = 25;
Console.WriteLine(myAge);

//  Reassignments cannot happen after initializations to other data types
//  myAge = " twenty five";
//  This code will not work as the variable myAge has now been 'locked' as an integer type.



//  LETS DO A BIT OF PRACTICE:
//  Storing values in variables
string practiceName = "Bob";
int practiceInt = 3;
float practiceFloat = 34.4F;

//Printing the stored values:
Console.Write("Hello, ");
Console.Write(practiceName);
Console.Write("! You have ");
Console.Write(practiceInt);
Console.Write(" messages in your inbox. The temperature is ");
Console.Write(practiceFloat);
Console.WriteLine(" celsius.");

// Note: There is a more easy way to do this, but for now I will stick to this
// since the easier way was not yet covered in theory.