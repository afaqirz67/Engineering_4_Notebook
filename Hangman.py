hanger = "---"+"┐" #Characters to draw hangman - each body part is associated with a specific name
head = "   O\n"
head2 = "   O"
armLeft = "  /"
body = "|"
rightArm = "\\\n"
body2 = "   |\n"
leftLeg = "  /"
rightLeg = " \\"

a = head    # a variable is assigned to set of body parts correlating the specefic number of times a wrong letter is entered
b = head + armLeft
c = head + armLeft + body
d = head + armLeft + body + rightArm
e = head + armLeft + body + rightArm + body2
f = head + armLeft + body + rightArm + body2 + leftLeg
g = head + armLeft + body + rightArm + body2 + leftLeg + rightLeg
                        #declaring new variables 
correctGuess= ''        #correct guess stores the correct inputs
missedGuess = ''        #missedGuess keeps track of wrong inputs
wrong = 0               

word = str(input("Player 1 enter your word: "))         #input is a string which is stored in variable "word"
print("\n" *5000)                                       #after input is recieved, this line will space out the next program output/input after 50 lines
blanks = '-' * len(word)                                #variable blanks is equal to dashes numbered based on letters of the word
blanks_list = list(blanks)                              #creats a list of the inputs stored in blanks variable

print("player two guess a letter: ")

while wrong < 8:                                       #the loop will run until the number of wrong guess hasn't reached 8
    guess = input("")                                  
    i = 0

    if guess not in word:                               #if the guessed letter is not in the word
        missedGuess = missedGuess+guess                 #guess is added to the variable missedGuess
        print("Oops! Wrong letter. Try Again! ")
        wrong+=1                                        #the counter is incremented by 1
        count = wrong                                   #count equals the value stored in wrong
        
        if count == 1:                                  #according to what the "wrong" counter is equal to, the following set of if statments will print the body parts
            print(hanger+"\n"+ a)
        if count == 2:
            print(hanger+"\n"+ b)
        if count == 3:
            print(hanger+"\n"+ c)
        if count == 4:
            print(hanger+"\n"+ d)
        if count == 5:
            print(hanger+"\n"+ e)
        if count == 6:
            print(hanger+"\n"+ f)
        if count == 7:
            print(hanger+"\n"+ g)
    else:
        print("guess is right")                     #if the entered letter is right, correctGuess will store the guess
        correctGuess = correctGuess + guess
        
        for i in range(0, len(word)):               #the for loop will cycle from the first letter of the word to the last letter spot
            if word[i] in correctGuess:             #to gets the right spot in the array
                blanks=blanks[:i]+word[i]+blanks[i+1:]      #the correct guess replaces the specific spot in the dashes' array
                print(blanks)
        if word in blanks:
           print("You Win!")
    if wrong >= 7:
        print("You lost!")
