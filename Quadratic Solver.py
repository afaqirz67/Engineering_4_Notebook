import math


def solve(a, b, c):                                         #defines the function solve and  takes three inputs
    discriminant = (b * b - 4 * a * c)                      #declares the formula and sets it equal to discernment
    if discriminant > 0:                                    #if the discriminant is greater then 0 it will execute the following code
        one = (-b + math.sqrt(b * b - 4 * a * c))/(2*a)     #declares the quadratic formula and assigns it to varaible
        two = (-b - math.sqrt(b * b - 4 * a * c))/(2*a)
        roots = [one, two]
        return roots
    elif discriminant == 0:                                 #if the discriminant is equal to 0, it will execute the follwing code
        one = (-b + math.sqrt(b * b - 4 * a * c))/(2*a)
        two = (-b - math.sqrt(b * b - 4 * a * c))/(2*a)
        roots = one
        return roots
    else:         
        roots = ""
        return roots
            
            


print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")



value = ""                                              #value equals an empty string
while value == "":
  
    a = int(input("Enter coeffiecient a:"))             # takes the input and stores them as a, b, and c
    b = int(input("Enter coeffiecient b: "))
    c = int(input("Enter coeffiecient c: "))
 
    roots = solve(a,b,c)                                #Gives in the inputs to the function solve and that returns in the roots
            
    if len(roots) == 2:                                 #if the number of root letters is 2
        print("There are two roots "+str(roots))        #it will print two roots
    elif len(roots) ==1:
        print("There is one root "+str(roots))
    else:
        print("There are no roots "+str(roots))
    value = input("Press Enter to run again, press x then Enter to quit") #if the input the variable "value" is Enter it will run the code again. If it's x it will quit the loop

print("Goodbye!")
