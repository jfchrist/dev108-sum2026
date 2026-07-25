# starting file for lab 6

#import nameformat module
import nameformat

#create title function
def title():
    print("The Name Program!\n")
#create main module to order processes
def main():
    title()
    #define user's first name
    firstName = input("What is your first name? ")
    #define user's last name
    lastName = input("What is your last name? ")
    print("\n// OPTIONS //\n1- Say Hello!\n2 - Output full name\n3 - Output last name, first name\n4 - Read documentation\n5 - Exit")
#ask what function user would like to proceed with and set in loop
#allow options for reading documentation and exiting program
    while (option := input("\nWhat would you like the program to do?: ")):
        if option.isdigit():
            option = int(option)
            if option == 1:
                nameformat.sayHello(firstName.capitalize())
            elif option == 2:
                nameformat.fullName(firstName.capitalize(), lastName.capitalize())
            elif option == 3:
                nameformat.lastNameFirst(lastName.capitalize(), firstName.capitalize())
            elif option == 4:
                help(nameformat.sayHello)
                help(nameformat.fullName)
                help(nameformat.lastNameFirst)
                continue
            elif option == 5:
                #create farewell message
                print("\nBye now!")
                break
            #filter for integer >5
            else:
                print(f"Sorry, {option} was not a provided option. Please try again.")
                continue
        #filter for non-integer input
        else:
            print("\nSorry, invalid input. Please try again")
            continue








main()