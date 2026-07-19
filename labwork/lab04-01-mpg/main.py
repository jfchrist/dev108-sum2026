# Starting file for Exercise 3-1
# display a welcome message
print("The Miles Per Gallon Program")
# get input from the user
while True:     #establish loop for incorrect answers or 2nd run of program
    print()
    miles_driven = float(input("Please enter miles driven:         "))
    gallons_used = float(input("Please enter gallons of gas used:  "))
    gallon_cost = float(input("Please enter cost per gallon:     "))
# validates user inputs
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
        continue
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
        continue
    elif gallon_cost <= 0:
        print("Gallon cost must be greater than zero. Please try again.")
        continue
    else:
    # inputs must be good
    # calculate and display miles per gallon
        print()
        print("==="*5)
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:   ", mpg)
    # calculate and display total gas cost
        total_cost = round(gallons_used*gallon_cost)
        print(f"Total Cost:         ${float(total_cost)}")
    #calculate and display cost per mile
        print(f"Cost per Mile:      ${round(total_cost/miles_driven,2)}")
        print("==="*5)
    #ask for loop
        answer = input("\nWould you like to enter information for another trip? y/n:  ")
        if answer.lower() == "y":
            continue
        else:
            break
print()
print("Good-Bye!")

