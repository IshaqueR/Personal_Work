/* You're developing a Student GPA Calculator that will
 * help calculate students' overall Grade Point Average. 
 * The parameters for your application are:
 * 
 * You're given the student's name and class information.
 * Each class has a name, the student's grade, and the number of credit hours for that class.
 * Your application needs to perform basic math operations to calculate the GPA for the given student.
 * Your application needs to output/display the student’s name, class information, and GPA.
 * 
 * To calculate the GPA:
 * Multiply the grade value for a course by the number of credit hours for that course.
 * Do this for each course, then add these results together.
 * Divide the resulting sum by the total number of credit hours.
 * 
 * You're provided with the following sample of a student's course information and GPA:
 * 
 * Student: Sophia Johnson
 * 
 * Course          Grade   Credit Hours	
 * English 101         4       3
 * Algebra 101         3       3
 * Biology 101         3       4
 * Computer Science I  3       4
 * Psychology 101      4       3
 * 
 * Final GPA:          3.35
 */

string studentName = "Sophia Johnson";
string course1Name = "English 101";
string course2Name = "Algebra 101";
string course3Name = "Biology 101";
string course4Name = "Computer Science I";
string course5Name = "Psychology 101";

int course1Credit = 3;
int course2Credit = 3;
int course3Credit = 4;
int course4Credit = 4;
int course5Credit = 3;

// Store the numeric grade values for each course

int gradeA = 4;
int gradeB = 3;
//int gradeC = 2; //unused
//int gradeD = 1;
//int gradeF = 0;

/*I'll be using these grades.
 * 
 * Course			    Grade		
 * English 101		     A
 * Algebra 101		     B
 * Biology 101		     B
 * Computer Science I	 B
 * Psychology 101	     A
 * 
 */

int course1Grade = gradeA;
int course2Grade = gradeB;
int course3Grade = gradeB;
int course4Grade = gradeB;
int course5Grade = gradeA;

// Calculate the sum of credit hours and grade points

int course1Value = course1Credit * course1Grade;
int course2Value = course2Credit * course2Grade;
int course3Value = course3Credit * course3Grade;
int course4Value = course4Credit * course4Grade;
int course5Value = course5Credit * course5Grade;

// Adding the results
int totalCourseSum = course1Value + course2Value + course3Value + course4Value + course5Value;

// Get the total number of credit hours
int totalCreditHours = course1Credit + course2Credit + course3Credit + course4Credit + course5Credit;

// Get GPA by dividing totalCourseSum by totalCreditHours
decimal gradePointAverage =  totalCourseSum / (decimal)totalCreditHours;

// Round the GPA to 2 decimal points
int leadingDigit = (int)gradePointAverage;
int firstDigit = (int)(gradePointAverage * 10) % 10;
int secondDigit = (int)(gradePointAverage * 100) % 10;

//Display the GPA with the Student information
Console.WriteLine($"Student: {studentName}\n");
Console.WriteLine($"Course\t\t\t\tGrade\t\tCredit Hours");
Console.WriteLine($"{course1Name} \t\t\t{course1Grade} \t\t{course1Credit}");
Console.WriteLine($"{course2Name} \t\t\t{course2Grade} \t\t{course2Credit}");
Console.WriteLine($"{course3Name} \t\t\t{course3Grade} \t\t{course3Credit}");
Console.WriteLine($"{course4Name} \t\t{course4Grade} \t\t{course4Credit}");
Console.WriteLine($"{course5Name} \t\t\t{course5Grade} \t\t{course5Credit}\n");

Console.WriteLine($"Final GPA: \t\t\t{leadingDigit}.{firstDigit}{secondDigit}");