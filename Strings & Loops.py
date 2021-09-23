# Python program to Print Characters in a String
 
str1 = input("Type in your text, then press Enter :") #the variable stores input as a String
i = 0                                                 #sets the couter equal to "0"

while(i < len(str1)):               #when the value of i is less than the count of characters stored in variable "str1" it executes the following lines
    if (str1[i] == " "):            #if if the character equals a space, 
        print("-")                  #it will print a dash to seperate the words
        i = i + 1                   #checks the next input character 
    else:
        print(( str1[i]))           #Otherwise it prints the stored string letter by letter
        i = i + 1                   #prints a charachter and moves to the next character
    
