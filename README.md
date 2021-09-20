# Engineering_4_Notebook

## TABLE OF CONTENTS
* [TABLE OF CONTENTS](#TABLE-OF-CONTENTS)
* [HELLO PYTHON](#HELLO-PYTHON)
* [PYTHON CALCULATOR](#PYTHON-CALCULATOR)

## HELLO PYTHON
```C
import random

print("Automatic Dice Roller")
value="" #variable for storing inputs

while value == "": //the statement is true while the value doesn't have any strings inside it
    r = random.randint(1, 6) //choose a random integer between the given limits
    value = input("Press Enter to roll, press x then Enter to quit")
    
    if value == "": //checks to see if the statement is still valid
        
        print(r)
        print("Roll the dice again?")
```

## PYTHON CALCULATOR

![python_calculator](https://user-images.githubusercontent.com/56890879/134016155-697fe1af-c13f-497c-bd74-a5b26f6fc654.png)

