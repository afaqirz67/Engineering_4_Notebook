# Engineering_4_Notebook

## TABLE OF CONTENTS
* [TABLE OF CONTENTS](#TABLE-OF-CONTENTS)
* [HELLO PYTHON](#HELLO-PYTHON)

## HELLO PYTHON
```C
import random

print("Automatic Dice Roller")
value=""

while value == "":
    r = random.randint(1, 6)
    value = input("Press Enter to roll, press x then Enter to quit")
    
    if value == "":
        
        print(r)
        print("Roll the dice again?")
```
