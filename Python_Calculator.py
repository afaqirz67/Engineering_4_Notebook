import math 

print("Calculator Program")

a = int(input("Enter your first number")) //takes the first input - stores the value in varaible a
b = int(input("Enter your second number")) //takes the second input - stores the value in varaible b

def doMath(a, b, c):  //the function takes 3 arguments - two which are the inputs and c is returing what math opertaion has to be done for the specific line of code
    if c == 1:        // if c == the given number -  it returns the value after doing the specific math operation its assigned to
        return a + b 
    if c == 2:
        return a - b 
    if c == 3:
        return a * b 
    if c == 4:
        return a / b 
    if c == 5:
        return a % b

print("Sum:\t\t" + str(doMath(a,b,1)))      //prints the output of doMath - 1 is assined to add, so a and b are added
print("Difference:\t" + str(doMath(a,b,2))) //2 is assined to subtract, so a and b are subtracted
print("Product:\t" + str(doMath(a,b,3)))
print("Quotient:\t" + str(doMath(a,b,4)))
print("Modulo:\t\t" + str(doMath(a,b,5)))
