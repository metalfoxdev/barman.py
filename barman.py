import os

# Ideas
# Keep list of choices and use the list to write the future
while(True):
    age = input("What is your age? - ")
    age = int(age)
    def cs():
        os.system("cls||clear")
    def question(q, sel):
        output = str()
        i = 1
        for x in range(len(sel)):
            output = output + "\n" + str(i) + ". " + o[int(x)]
            i = i + 1
        output = q + "\n" + output
        return output
    cs()
    if age > 17:
        print("What can i get for you young sir?")
        print(question("What can i get for you young sir?", ["beer","wine","lagar"]))
        va = False
        while va == False:
            answer = input("Enter your choice - ")
            answer = int(answer)
            cs()
            if answer == 1:
                choice = "beer"
                input("So you want a beer eh? \nPress ENTER to Continue...")
                va = True
                branch = answer
                cs()
            elif answer == 2:
                choice = "wine"
                input("AAAAAAAH! I see you want a wine, what type? \nPress ENTER to Continue...")
                va = True
                branch = answer
                cs()
            elif answer == 3:
                choice = "lagar"
                input("I see you want to have the legendary lagar! Drink and enjoy! \nPress ENTER to continue...")
                va = True
                branch = answer
                cs()
            else:
                print("I don't have that on the menu")
                print(question(selections))
                print("------------------------------------------------------------------")
                va = False
                cs()
        va = False
        while va == False:
            print("What will you do?")
            if branch == 1:
                print(question(["Hit the person beside you with your bottle of beer","Smash your beer bottle and ask for another","Drink your beer and leave"]))
            elif branch == 2:
                    print(question(["White","Red"]))
                    answer = input("Enter your choice - ")
                    if answer == 1:
                        input("White wine it is! \nPress ENTER to continue...")
                        # implement branching
                    elif answer == 2:
                        input("Red wine, good choice! \nPress ENTER to continue...")
                        # implement branching
                    else:
                        print("You can't do that. \nPress ENTER to Continue...")
                        print(question(["White","Red"]))
                        print("------------------------------------------------------------------")
                        va = False
                        cs()
    else:
        print("Go home boy!")
        print("------------------------------------------------------------------")

