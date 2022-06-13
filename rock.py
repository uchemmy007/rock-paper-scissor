from random import choice

options = ["R", "P", "S"]

computer = choice(options)

player = False

while player == False:

    player = input("R, P, S?")
    if player == computer:
        print("Tie!")
        player = False
        computer = choice(options)
   
    elif player == "R":
        if computer == "P":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "P":
        if computer == "S":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
           
    elif player == "S":
        if computer == "R":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
         
    else:
        print("That's not a valid play. Check your spelling!")
        player = False
        computer = choice(options)
   