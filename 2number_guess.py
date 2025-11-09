name = input("Hello!! What is your name?")
print("ok",name,"let's play a game!!")
mode = input("Enter Difficulty level Type Hard or Easy")
if(mode == "HARD"or"Hard"or"hard"):
    print("Guess the number between 0 to 100")
    import random

    num = random.randint(1,100)
    if (num>50):
       print("high")
    elif(num<50):
        print("low") 
    guess = int(input("Enter Your Number - "))
    print("Your Guess -",guess,"Our Number",num)
    if (guess==num):
        print("Yoo Correct!!!")
    elif(guess!=num):
        print("Try Again :( ")
    else :
        print("Enter Valid Details")
elif(mode == "EASY"or"Easy"or"easy"):
    print("Guess the number between 0 to 10")
    import random

    num = random.randint(1,10)
    if (num>5):
       print("high")
    elif(num<5):
        print("low") 
    guess = int(input("Enter Your Number - "))
    print("Your Guess -",guess,"Our Number",num)
    if (guess==num):
        print("Yoo Correct!!!")
    elif(guess!=num):
        print("Try Again :( ")
    else :
        print("Enter Valid Details")
#           ADVANCE LEVELS
# Limit the number of guesses (e.g., only 10 chances).
# Display a “Game Over” message if you run out of chances.  
# Keep track of high scores (fewest attempts).