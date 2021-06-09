#taylor levy
#writing a game menu
varChoice = " "
def menu():
    print("*"*28)
    print("*"," "*6,"Forerunner"," "*6,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"L1- Two Betrayls"," "*4,"*")
    print("*"," "*2,"L2- Sacred Icon"," "*5,"*")
    print("*"," "*2,"L3- The Storm"," "*7,"*")
    print("*"," "*2,"EX- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,or EX", end=" ")
    varChoice = input ()
    return varChoice
def score ():
    print ("Your score")
    print ("8473      Taylor")
    print ("9169      Tatum")
    print ("8409      Ms. Suarez")
def gamePause ():
    print ("do you want to change levels?")
    level = input ()
    if level !='no':
        varChoice=menu ()
varChoice = menu ()

varChoice = input ()
while varChoice !="EX":
    if varChoice=="L1":
        print ("You are in level 1")
        gamePause ()
    if varChoice=="L2":
        print ("You are in level 2")
    if varChoice=="L3":
        score ()
    varChoice=menu()
print("Goodbye, Have a nice day")