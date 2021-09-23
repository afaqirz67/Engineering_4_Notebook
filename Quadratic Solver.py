import math


def solve(a, b, c):                                     #defines the function solve and  takes three inputs
    discernment = (b * b - 4 * a * c)                   #declares the formula and sets it equal to 
    if discernment > 0:
        one = (-b + math.sqrt(b * b - 4 * a * c))/(2*a)
        two = (-b - math.sqrt(b * b - 4 * a * c))/(2*a)
        roots = [one, two]
        return roots
    elif discernment == 0:
        one = (-b + math.sqrt(b * b - 4 * a * c))/(2*a)
        two = (-b - math.sqrt(b * b - 4 * a * c))/(2*a)
        roots = one
        return roots
    else:         
        roots = ""
        return roots
            
            


print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")



value = ""
while value == "":
  
    a = int(input("Enter coeffiecient a:"))
    b = int(input("Enter coeffiecient b: "))
    c = int(input("Enter coeffiecient c: "))
 
    roots = solve(a,b,c)        
            
    if len(roots) == 2:
        print("There are two roots "+str(roots))
    elif len(roots) ==1:
        print("There is one root "+str(roots))
    else:
        print("There are no roots "+str(roots))
    value = input("Press Enter to run again, press x then Enter to quit")

print("Goodbye!")
