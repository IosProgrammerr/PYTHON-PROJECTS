import random

game = ["rock", "paper", "scissor"]
computer = random.choice(game)
rund = int(input("ENTER HOW MANY ROUNDS YOU WANT TO PLAY - "))
chance = int(input("ENTER HOW MANY LIFELINE YOU WANT TO PLAY - "))
while chance > 0 and rund > 0 :
    computer = random.choice(game)
    print(computer)
    user = input("Enter ROCK, PAPER or SCISSOR: ").lower()

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
        rund -=1
    elif (user == "rock" and computer == "scissor") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissor" and computer == "paper"):
        print("🎉 Congratulations, You WON!")
        rund -=1
    elif (computer == "rock" and user == "scissor") or \
        (computer == "paper" and user == "rock") or \
        (computer == "scissor" and user == "paper"):
        print("BETTER LUCK NEXT TIME...")
        chance -= 1 
        rund -= 1
    else:
        print("Invalid input! Please enter rock, paper or scissor.")
