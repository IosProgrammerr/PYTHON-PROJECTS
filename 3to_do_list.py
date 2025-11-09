# THERE IS ONLY ONE ISSUE IN THIS CODE WHEN WE COMMAND  AND WANT TO COMPLETE A TASK THE TASK WILL BE SHOWN TWO TIMES
while True:
    a = int(input("ENTER 1 TO VIEW TASK \nENTER 2 TO ADD A NEW TASK \nENTER 3 TO MARK A TASK AS DONE \nENTER 4 TO DELETE A TASK \nENTER 5 TO EXIT \nGIVE US COMMAND :- "))
# print(a)
    if(a==1):
        f = open("/Users/kunal/Projects/Level-1/3task.txt","r")
        data = f.read()
        print(data)
        f.close()
    elif(a==2):
        task = input("ENTER YOUR TASK - ")
        f = open("3task.txt","a")
        data = f.write("\n" + task) #(task + "\n") i google it that how to pass two arguments and the answer is simple yo can simply add them if it makes logic simpple
        print("THIS IS YOUR TASK - ",task,"WE ARE SAVING IT..")
        f.close()
    elif(a==3):
        with open("3task.txt","a+")as f:    #find with syntax from notes
            f.seek(0)   #i have google this line  because without this line my data is not printing because the cursor will go at the end and i have to print my data this line help to go cursor at the starting
            data = f.read()
            print(data)
            done = input("ENTER THAT TASK YOU HAVE DONE..")
            data = f.write(done +" - done ☑️ \n")
            f.seek(0)
            data = f.read()
            print(data)
    elif(a==4):
        with open("3task.txt", "r+") as f:
            f.seek(0)
            data = f.read()
            print("Your current tasks:")
            print(data)
            brust = input("ENTER THE TASK YOU WANT TO DELETE: ")
            # Replace the task with nothing (delete it)
            new_data = data.replace(brust, "")
            # Go back to start of file and rewrite
            f.seek(0)
            f.write(new_data)
            f.truncate()  # i google this line
            print("Task deleted successfully ✅")
    elif (a==5):
        print("PROGRAM ENDED")
        break
    else:
        print("ENTER INVALID DATA")
# SOME ADVANCE THINGS TO ADD
# WE CAN ADD HIGH OR LOW Pvt. LEVEL WORK
# WE CAN ALSO ADD LABELS LIKE THIS ACOORDING TO WORK FOR EXAMPLE - 🔴/🟢
# WE CAN ADD DATE ON TASK AND IT SHOULD BE MENTIOND THAT THIS TASK WILL BE URGENT ON THAT SPECEFIC DATE