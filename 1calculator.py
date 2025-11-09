print("Our Calc can perform multiple task like :- \n Type + for addition \n Type - for Subtraction \n Type * for Multiplication \n Type / for Division")
num1 = int(input("Enter Your First Digit :- "))
action = input("Enter Your Action  Which You Want To Perform :- ")
num2 = int(input("Enter Your Second Digit :- "))
if (action == "+"):
    print(num1 + num2)
elif (action == "-"):
    print(num1 - num2)
elif (action == "*"):
    print(num1 * num2)
elif (action == "/"):
    print(num1 / num2)
else :
    print("Print valid Details")