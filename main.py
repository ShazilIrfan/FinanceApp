import time #Add pacing between code

# Creating menu class
class menu:

    #Setting while loop to true
    flag = True
    pace = time.sleep(0.4)

    def __init__(self):
        pass


    #Visually display menu
    def displaymenu(self):
        print("--- Finance Tracker --- ")
        self.pace
        print()
        self.pace

        #Starting while loop
        while self.flag:
            print("Display Finances (1)")
            self.pace
            print("Add Finances (2)")

            self.pace
            print()
            self.pace

            #Doing error checks for the correct value inputted
            try:
               self.userchoice = input("Select an option: ")
               self.choicecheck = int(self.userchoice)

               self.usercheck()
               self.pace

            except ValueError:
                self.pace
                print()
                self.pace
                print("Please select a visible number")
                self.pace
                print()
                self.pace
                continue

            #Asking user to return to the start or exit program
            self.user_return = input("Go back to menu?: ").lower()
            self.menureturn()


    #Creating the logic for looping back to menu
    def menureturn(self):
        print()
        self.pace
        
        if self.user_return in ("yes", "y"):
            pass
            print()
            self.pace

        elif self.user_return in ("no", "n"):
            self.flag = False

        else:
            self.pace
            print("Select (y) or (n)")
            print()
            self.pace


    #Checking user's option and giving the appropriate response
    def usercheck(self):
        if self.choicecheck == 1:
            print()

            self.pace
            print("Option one works")
            self.pace

            print()
            self.pace

            self.flag = False

        elif self.choicecheck == 2:
            print()

            self.pace
            print("Option two works")
            self.pace

            print()
            self.pace

            self.flag = False

        else:
            print()

            self.pace
            print("Select (1) or (2)")
            self.pace

            print()
            self.pace
            
            



# Start Program
main = menu()
main.displaymenu()
