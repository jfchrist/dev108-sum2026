#Jaine Christ
#8/6/2026
#Dev 108
#Final Project--Battle Simulator

import csv
import random

#create character function
def generate():
    pass

#menu for saving/searching/deleting characters
def menu():
    print("""
\t-- MENU --
Create a random character:\t1
List saved characters:\t\t2    
Display character's details:\t3
Delete a character:\t\t4
Battle characters:\t\t5
Exit:\t\t\t\t6
\t----------""")
    choice = input("What would you like to do?")
    return choice


#battle simulation
def battle():
    pass

def main():
    print("* * *"*4)
    print("Character Generator Battle Simulator")
    print("* * *"*4)

    while True:
    #run menu and ask about that 
        option = menu()

        if option == "1":
            generate()
            continue
        elif option == "2":
            
            continue
        elif option == "3":
            
            continue
        elif option == "4":
            
            continue
        elif option == "5":
            battle()
            continue
        elif option == "6":
            print("Good-bye!")
            continue
        else:
            print("invalid")
            continue
    else:
        print("bye")

main()