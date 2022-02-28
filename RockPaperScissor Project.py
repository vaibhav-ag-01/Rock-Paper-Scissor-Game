import random

game_list=["Rock","Paper","Scissor"]

c=0
p=0

while(True):
    player = input("Enter Rock, Paper or Scissor or Quit : ")
    computer = random.choice(game_list)

    print()
    print("Computer chose : {}".format(computer))
    print("Player chose : {}".format(player))
    print()
    
    if(player == "Quit"):
        break

    elif(player == computer):
        print("Tie")

    elif(player == "Rock"):
        if(computer == "Paper"):
            c+=1
            print("Computer Won!")
        else:
            p+=1
            print("Player Won!")

    elif(player == "Paper"):
        if(computer == "Scissor"):
            c+=1
            print("Computer Won!")
        else:
            p+=1
            print("Player Won!")

    elif(player == "Scissor"):
        if(computer == "Rock"):
            c+=1
            print("Computer Won!")
        else:
            p+=1
            print("Player Won!")
    
    else:
        print("Incorrect Input! \nTry Again")

    
    print()
    print("Computer = {} Player = {}".format(c,p))
    print()
