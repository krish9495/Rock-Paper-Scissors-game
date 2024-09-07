import random
computer = random.choice([0,-1,1])
your = input("Enter R,P or S\n")

youdict={"R":1,"P":0,"S":-1}
reversedict={1:"R",0:"P",-1:"S"}
comp=reversedict[computer];
if(comp==your):
    print("It's a tie")
else:
    if(your=="S" and comp=="R"):
        print("Computer Wins!!")
    elif(your=="S" and comp=="P"):
        print("You Wins!!")
    elif(your=="R" and comp=="S"):
        print("You Wins")
    elif(your=="R" and comp=="P"):
        print("Comp Wins")
    elif(your=="P" and comp=="S"):
        print("Comp Wins!!")
    elif(your=="P" and comp=="R"):
        print("You Wins")
    else:
        print("Something went wrong")

