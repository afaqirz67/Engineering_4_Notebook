letters= ["A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"]

start = ("---┐")
head  = (" o")
leftArm = ("\ ")
upBody = ("|")
rightArm = ("/")
lowerBody = ("|")
leftLeg = ("/")
rightLeg = ("\ ")
print("---┐")
print("   o")
print("  \|/")
print("   | ")
print("  / \ ")

while True:    
    for i in range(1):
        guessWord = str(input("player1 enter your word:"))
        length_of_word=len(guessWord)
        display=("-"*length_of_word)

    print(str(start))
    print("")
    print("Missed Letters:")
    print("")
    print(display)
    
    for i in range(1):
        letter_guess=str(input("Please guess a letter:"))
        if letter_guess in guessWord:
            #display=display.rstrip(display)
