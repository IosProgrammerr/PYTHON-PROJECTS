while True:                         # while = loop keyword, True = always true → loop runs forever
                                    # This creates an infinite loop until we break it.

    print("1 -> ADD CONTACTS")      # print() shows menu options on screen
    print("2 -> VIEW CONTACTS")
    print("3 -> SEARCH CONTACTS")
    print("4 -> UPDATE CONTACTS")
    print("5 -> DELETE CONTACTS")
    print("6 -> EXIT")

    cmd = int(input("TYPE YOUR COMMAND - ")) 
                                    # input() → take user input as string
                                    # int() → convert the input into an integer number
                                    # cmd variable stores user's choice (1–6)

    if (cmd==6):                    # if user enters 6
        break                       # break exits the while loop → program ends

    elif (cmd==1):                  # elif = else-if, runs only if previous if is false
                                    # cmd == 1 means user wants to ADD A CONTACT
        createnme = input("ENTER NAME - ")      # take contact name → store in createnme
        createnum = input("ENTER PHONE NUMBER - ")  # take phone number
        createid  = input("ENTER EMAIL-ID - ")      # take email id
        createadd = input("ENTER YOUR ADDRESS - ")  # take address

        key = {"NAME" : createnme,                 # creating a dictionary "key"
               "PHONE" : createnum,                # left side = key name, right side = variable value
               "GMAIL":createid,
               "ADDRESS":createadd}

        cnfrm = input("TYPE [Y] TO ADD CONTACT - ")  # asks user to confirm addition

        if (cnfrm == "y" or "Y"):  # WRONG LOGIC but unchanged because you asked not to modify
                                    # This condition always becomes true.
            f = open("1contact.txt","a")            # open() = open file
                                                    # "1contact.txt" = file name
                                                    # "a" = append mode (add new text at bottom)
            
            data = f.write("\n" + createnme +"\n" + createnum +"\n" + createid +"\n" + createadd + "\n")
                                    # f.write() writes text into the file
                                    # "\n" creates a new line
                                    # writing 4 lines: name → number → email → address

            print("THIS IS YOUR CONTACT - \n",createnme,createnum,createid,createadd,"\n FINALLY ADDED")
                                    # show contact details on screen

            f.close()               # close file after writing

        else:                       # if cnfrm is not Y (but this never runs)
            print("OK! WE ARE NOT SAVING YOUR DATA...")

    elif (cmd==2):                  # VIEW CONTACTS option
        f = open("1contact.txt","r")  # open file in read mode "r"
        data = f.read()                # read() = read entire file as a single string
        f.close()                      # close file
        print(data)                    # print entire contact list

    elif (cmd == 3):                # SEARCH contact
        search = input("Enter word to search: ")  
                                    # store word to search for in the file

        f = open("1contact.txt", "r") # open file for reading
        lines = f.readlines()         # readlines() = returns list of ALL lines in file
        f.close()                     # close file

        for i in range(len(lines)):   # for loop → i goes from 0 to total number of lines - 1
            if search in lines[i]:    # "in" checks if the search word exists inside the line
                
                print("FOUND! Printing 4 lines:\n")

                for j in range(i, i + 4):        # print contact block → 4 lines
                    if j < len(lines):           # avoid going out of file range
                        print(lines[j].strip())  # strip() removes extra newline spaces
                break                             # break → stop search after first match
        else:
            print("WORD NOT FOUND.")             # else after for loop = executed when loop has no break

    elif (cmd == 4):                  # UPDATE CONTACT
        search = input("Enter contact: ").strip().lower()
                                    # .strip() removes spaces, .lower() makes everything lowercase  
        
        found_index = -1            # -1 means "not found yet"

        with open("1contact.txt", "r") as f:  
                                    # with = auto closes file
            lines = f.readlines()   # read file into list

        for i in range(len(lines)): # search the entire file
            if search in lines[i].lower():  # find matching line (case-insensitive)
                found_index = i             # store index where contact starts
                break                       # stop when found

        if found_index == -1:               # if still -1 → not found
            print("WORD NOT FOUND...")
            exit()                          # exit program

        print("\nFOUND! Printing 4 lines:\n")
        for j in range(found_index, found_index + 4):
            if j < len(lines):              # avoid index error
                print(lines[j].strip())     # print contact block

        update = input(                     # ask user what field to update
            "\nENTER WHAT YOU WANT TO UPDATE :-\n"
            "Press 'n' to update Name\n"
            "Press 'p' to update phone number\n"
            "Press 'g' to update gmail\n"
            "Press 'a' to update address\n"
        ).lower()                           # making user input lowercase

        index_map = {"n": 0, "p": 1, "g": 2, "a": 3}
                                    # dictionary: maps input → line offset

        if update not in index_map:        # if wrong input
            print("Invalid choice!")
            exit()

        old_line_index = found_index + index_map[update]
                                    # calculate which line to update
                                    # example: if updating phone → found_index + 1

        new_text = input("Enter new text: ").strip()  
                                    # take updated value

        lines[old_line_index] = new_text + "\n"  
                                    # replace old line with new value

        with open("1contact.txt", "w") as f:
                                    # open file in write mode → clears entire file
            f.writelines(lines)     # write updated list back to file

        print("Contact updated successfully!")

    elif (cmd == 5):                # DELETE CONTACT
        search = input("Enter contact: ").strip().lower()

        found_index = -1
        with open("1contact.txt", "r") as f:
            lines = f.readlines()

        for i in range(len(lines)):         # search contact
            if search in lines[i].lower():
                found_index = i
                break

        if found_index == -1:               # if not found
            print("WORD NOT FOUND...")
            continue                         # go back to menu

        print("\nFOUND! Printing 4 lines:\n")
        for j in range(found_index, found_index + 4):
            if j < len(lines):
                print(lines[j].strip())

        confirm = input("Are you sure you want to delete this contact? [Y/n]: ").trim().lower()
                                    # confirmation before deleting

        if confirm != "y":          # if user did NOT type y
            print("Delete cancelled.")
            continue                # go back to menu

        del lines[found_index: found_index + 4]  
                                    # delete all 4 lines of this contact

        with open("1contact.txt", "w") as f:
            f.writelines(lines)     # write remaining lines back

        print("Contact deleted successfully!")
