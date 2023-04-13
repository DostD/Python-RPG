__version__ = '0.1.0'

# Fuctions
weapon = False
def showDarkroom():
    directions = ["forward", "backward"]
    print("You see a body of a fellow employee, you bow your head.")
    print("Where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: forward/backward")
        userinput = input()
        if userinput == "forward":
            print("You made it! you found one of the ways to the control room. Time to make your escape")
        elif userinput == "backward":
            showUNIDENTIFIED()
        else:
            print("Please enter a valid option")

def showUNIDENTIFIED():
    directions = ["right", "left", "backward"]
    print("You see some sort of figure you can't really explain. You are creeped out.")
    print("Where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: right/left/backward")
        userinput = input()
        if userinput == "right":
            showDarkroom()
        elif userinput == "left":
            print("You find open a door that leads to a wall")
        elif userinput == "backward":
            introscene()
        else:
            print("Please enter a valid option")  

def showHallway():
    actions = ["fight", "flee"]
    global weapon
    print("You enter into the hallway and see a dark creature. You can try to fight or you can flee.")
    print("What will you do?")
    userinput = ""
    while userinput not in actions:
        print("Options: fight/flee")
        userinput = input()
        if userinput == "fight":
            if weapon:
                print("You bring out your Lazer Sword that you found and kill the creature. What do you know the creature was blocking")
                print("the control room, time to get out of here. Congrats you win!")
            else:
                print("You have no weapon to fight with so you lost the battle and the creature killed you.")
        elif userinput == "flee":
            introscene()
        else:
            print("Please enter a valid option")

def showGoodroom():
    directions = ["right", "left", "backward"]
    global weapon
    print("You enter into to a room that seems to be good beside the creepy voices... maybe there is some snacks here")
    print("Where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: right/left/backward")
        userinput = input()
        if userinput == "right":
            print("...Remember those creepy voices? Well it turns out they are ghost of dead employees... and they what your body")
            print("...and your stuck in a room with them. YOU DIED")
        elif userinput == "left":
            print("Oh look a sandwich yum, and a lazer sword... you should take that and leave.   Weapon Collected")
            print("You go back to the main room")
            weapon = True
            introscene()
        elif userinput == "backward":
            introscene()
        else:
            print("Please enter a valid option")
      
def introscene():
    directions = ["left", "right", "forward", "backward"]
    print("You are at a crossroad of 4 options on where to go, where will you go?")
    userinput = ""
    while userinput not in directions:
        print("Options: left/right/forward/backward")
        userinput = input()
        if userinput == "left":
            showUNIDENTIFIED()
        elif userinput == "right":
            showGoodroom()
        elif userinput == "forward":
            showHallway()
        elif userinput == "backward":
            print("You just walked into a wall in the same room you are already in... Why?")
            print("maybe leave the room this time Mr." + name)
            introscene()
        else:
            print("Please enter a valid option")
            

# Intro Code
print("Can't start an adventure without a knowing who you are, now who are you?")
name = input()
print("Welcome to the Spaceship Atlas Mr." + name + ".")
print("If you don't already know we are currently being invaded by... UNIDENTIFIED,")
print("you need to get out of here by any means necassary Employee")
print("I suggest finding a way to the control room to get to a escape pod... Off you go!")
introscene()