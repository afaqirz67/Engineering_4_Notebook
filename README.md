# Engineering_4_Notebook

## TABLE OF CONTENTS
* [TABLE OF CONTENTS](#TABLE-OF-CONTENTS)
* [HELLO PYTHON](#HELLO-PYTHON)

## HELLO PYTHON
```C
import random

print("Automatic Dice Roller")
value=""

while value == "": #the statement is true while the value doesn't have any strings inside it
    r = random.randint(1, 6) #choose a random integer between the given limits
    value = input("Press Enter to roll, press x then Enter to quit")
    
    if value == "": #checks to see if the statement is still valid
        
        print(r)
        print("Roll the dice again?")
```
