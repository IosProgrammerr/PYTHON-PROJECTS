ques1 = "Is Python case sensitive when dealing with identifiers?"
q1a = "no"
q1b = "yes"
q1c = "machine dependent"
q1d = "none of the mentioned"
ques2 = "Which of the following is the correct extension of the Python file?"
q2a = ".python"
q2b = ".pl"
q2c = ".py"
q2d = ".p"
ques3 = "Is Python code compiled or interpreted?"
q3a = "Python code is both compiled and interpreted"
q3b = "Python code is neither compiled nor interpreted"
q3c = "Python code is only compiled"
q3d = "Python code is only interpreted"
ques4 = "Which keyword is used for function in Python language?"
q4a = "Function"
q4b = "def"
q4c = "Fun"
q4d = "Define"
ques5 = "Which of the following character is used to give single-line comments in Python?"
q5a = "double slash"
q5b = "single slash"
q5c = "inverted comma"
q5d = "hashtag"

mcq = {
    ques1 : [q1a,q1b,q1c,q1d],
    ques2 : [q2a,q2b,q2c,q2d],
    ques3 : [q3a,q3b,q3c,q3d],  #list and all questions and options
    ques4 : [q4a,q4b,q4c,q4d],
    ques5 : [q5a,q5b,q5c,q5d],
}
sol = {
    ques1 : [q1b],
    ques2 : [q2c],
    ques3 : [q3d],              #list and all are correct answer only
    ques4 : [q4b],
    ques5 : [q5d],
}
print("YOU HAVE TO TYPE YOUR ANSWER AS IT IS GIVEN IN OPTION ")
for key,value in mcq.items():
    print(key)
    for option in value:
        print(option)
    answer = input("ENTER YOUR ANSWER -")
     # a = answer==q1b   ->  simple but we got long syntax and didn't learn new thing
    if (answer==sol[key][0]):
        print("correct")
    else:
        print("wrong")

#we have to add a new feature that is the user got only 2 chance for correct answer
#we can add score of user