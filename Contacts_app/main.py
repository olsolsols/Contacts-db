import readMembers 
import addMembers 
import updateMembers 
import deleteMembers 

# create a function with menu options
def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5"]:
        print("\nMenu Options")
        print("1. Print Members details")
        print("2. Add a new member")
        print("3. Update members details")
        print("4. Delete a member")
        print("5. Exit")
        options = input("\n Enter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5"]:
            print("Not in the list of options")
    return options

#create a variable with a boolean value set to true
mainProgram = True


while mainProgram == True:
    #pass menuOption function to the variable main menu which will display the menu options
    mainMenu = menuOptions()
    
    if mainMenu == "1":
        readMembers.showRecords()
    elif mainMenu == "2":
        addMembers.addMembers()
    elif mainMenu == "3":
        updateMembers.update()
    elif mainMenu == "4":
        deleteMembers.delRecord()
    else:
        mainProgram == False
input("Press enter to exit")



# execrise add the options for user to:
#Add a member
#Update a member ----> written from line 31




# menuOptions()