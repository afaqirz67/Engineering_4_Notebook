import random

print("Automatic Dice Roller")
value=""
   # the random variable choose a rondom intrger between the given int
while value == "":
    r = random.randint(1, 6) 
    value = input("Press Enter to roll, press x then Enter to quit")
    
    if value == "": # the random variable choose a rondom intrger between the given int
        print(r)
        print("Roll the dice again?")

