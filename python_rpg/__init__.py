__version__ = '0.1.0'
import introstory

# Fuctions
def exposite(text:tuple):
    for paragraph in text:
    # if not the last paragraph, add a ... (press enter to continue)
        if paragraph != text[-1]:
            input(paragraph + " \n\033[3m\033[92mPress enter to continue...\033[0m")
        else:
            input(paragraph)

def get_menu_choice(menu: str, legal_choices: tuple) -> str:
    user_choice = ""
    while user_choice not in legal_choices:
        print(menu)
        user_choice = input("Your Choice: ")
        #Give feedback if user didn't use proper choice
        if user_choice not in legal_choices:
            print("Sorry, that is not an option, please select one of the following: ")
            print(legal_choices)
        return user_choice

weapon = False

def showDarkroom():
    print("You see a body of a fellow employee, they were only door away from the control room. you bow your head to honor your fellow crewmate.")
    menu = "\nYou have come across a crossroad of options:\n\n\t1 - Forward\n"
    menu += "\t2 - Backward\n"
    selection = get_menu_choice(menu, ("1", "2"))
    print(f"\nYou selected: {selection}")
    if selection == "1":
        print("You made it! you found one of the ways to the control room. Time to make your escape")
    elif selection == "2":
        showAlien()
    else:
        print("Please enter a valid option")

def showAlien():
    print("You see some sort of figure you can't really explain. You are creeped out.")
    menu = "\nYou have come across a crossroad of options:\n\n\t1 - Right\n"
    menu += "\t2 - Left\n\t3 - Backward\n"
    selection = get_menu_choice(menu, ("1", "2", "3"))
    print(f"\nYou Selected: {selection}")
    if selection == "1":
        showDarkroom()
    elif selection == "2":
        print("You find open a door that leads to a wall")
    elif selection == "3":
        introscene()
    else:
        print("Please enter a valid option")  

def showHallway():
    global weapon
    print("You enter into the hallway and see a Dra'Kesh. You can try to fight or you can flee.")

    menu = "\nWhat will you do?:\n\n\t1 - Fight\n"
    menu += "\t2 - Flee\n"
    selection = get_menu_choice(menu, ("1", "2"))
    print(f"\nYou Selected: {selection}")
    if selection == "1":
        if weapon:
            print("You bring out your Lazer Sword that you found and kill the Dra'Kesh. What do you know the Dra'Kesh was blocking")
            print("the control room, time to get out of here. Congrats you win!")
        else:
            print("You have no weapon to fight with so you lost the battle and the Dra'Kesh killed you.")
    elif selection == "2":
        introscene()
    else:
        print("Please enter a valid option")

def showGoodroom():
    global weapon
    print("You enter into to a room that seems to be good beside the creepy voices... maybe there is some snacks here")

    menu = "\nYou have come across a crossroad of options:\n\n\t1 - Left\n"
    menu += "\t2 - Right\n\t3 - Forward\n"
    selection = get_menu_choice(menu, ("1", "2", "3"))
    print(f"\nYou Selected: {selection}")

    if selection == "1":
        print("...Remember those creepy voices? Well it turns out they are ghost of dead employees... and they what your body")
        print("...and your stuck in a room with them. YOU DIED")
    elif selection == "2":
        print("Oh look a sandwich yum, and a lazer sword... you should take that and leave.   Weapon Collected")
        print("You go back to the main room")
        weapon = True
        introscene()
    elif selection == "3":
        introscene()
    else:
        print("Please enter a valid option")
      
def introscene():
    menu = "\nYou have come across a crossroad of options:\n\n\t1 - Left\n"
    menu += "\t2 - Right\n\t3 - Forward\n \t4 - Backward\n\n"
    selection = get_menu_choice(menu, ("1", "2", "3", "4"))
    print(f"\nYou Selected: {selection}")

    if selection == "1":
        showAlien()
    elif selection == "2":
        showGoodroom()
    elif selection == "3":
        showHallway()
    elif selection == "4":
        print("You just walked into a wall in the same room you are already in... Why?")
        print("maybe leave the room this time.")
        introscene()
    else:
        print("Please enter a valid option")


#Intro Code
if __name__ == "__main__":
    exposite(introstory.introduction)
    introscene()