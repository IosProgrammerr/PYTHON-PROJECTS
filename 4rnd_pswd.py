#HERE IN THIS CODE WE MADE A RANDOM PASSWORD GENERATOR FOR OUR USER...
print("ANSWER [Y] FOR TRUE AND [F] FOR FALSE")
lnth = int(input("ENTER HOW MANY DIGIT PASSWORD YOU WANT - "))
alphabet = input("DO YOU WANT THAT PASSWORD CONTAINS ALPHABET - ")
digit = input("DO YOU WANT THAT PASSWORD CONTAINS NUMBERS - ")
case = input("DO YOU WANT THAT PASSWORD CONTAINS UPPER & LOWER CASE LETTERS - ")
symbol = input("DO YOU WANT THAT PASSWORD CONTAINS SPECIAL CHARACTERS - ")
import random
import string
if (alphabet=="Y" and digit=="Y"and case=="Y"and symbol=="Y"):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=lnth))
    print(password)
elif(alphabet=="N"and digit=="Y"and case=="Y"and symbol=="Y"):
    password = ''.join(random.choices(string.digits + string.punctuation, k=lnth))
    print(password)
elif(alphabet=="Y"and digit=="N"and case=="Y"and symbol=="Y"):
    password = ''.join(random.choices(string.ascii_letters + string.punctuation, k=lnth))
    print(password)
elif(alphabet=="Y"and digit=="Y"and case=="N"and symbol=="Y"):
    caps = input("ENTER [Y] FOR CAPITAL LETTER AND [N] FOR SAMALL LETTER")
    if(caps == "Y"):
        password = ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k=lnth))
        print(password)
    elif(caps == "N"):
        password = ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=lnth))
        print(password)
    else:
        print("ENTER VALID DETAILS...")
elif(alphabet=="Y"and digit=="Y"and case=="Y"and symbol=="N"):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=lnth))
    print(password)
elif(alphabet=="N"and digit=="N"and case=="N"and symbol=="N"):
    print("ENTER VALID DETAILS PLEASE...")
elif(alphabet=="N"and digit=="N"and case=="N"and symbol=="Y"):#we have to make condition according to this line
    password = ''.join(random.choices(string.punctuation, k=lnth))
    print(password)
elif(alphabet=="Y"and digit=="N"and case=="N"and symbol=="N"):
    caps = input("ENTER [Y] FOR CAPITAL LETTER AND [N] FOR SAMALL LETTER")
    if (caps=="N"):
        password = ''.join(random.choices(string.ascii_lowercase , k=lnth))
        print(password) 
    elif(caps=="Y"):
        password = ''.join(random.choices(string.ascii_uppercase , k=lnth))
        print(password)
    else:
        print("PLEASE ENTER VALID DETAILS...")
elif(alphabet=="N"and digit=="Y"and case=="N"and symbol=="N"):
    password = ''.join(random.choices(string.digits, k=lnth))
    print(password)
elif(alphabet=="N"and digit=="N"and case=="Y"and symbol=="N"):
    print("YOU HAVE TO CHOOSE ALPHABETS FOR UPPER AND LOWER CASE")
elif(alphabet=="Y"and digit=="N"and case=="Y"and symbol=="N"):
    password = ''.join(random.choices(string.ascii_letters, k=lnth))
    print(password)
elif(alphabet=="N"and digit=="Y"and case=="N"and symbol=="Y"):
    password = ''.join(random.choices(string.punctuation + string.digits, k=lnth))
    print(password)