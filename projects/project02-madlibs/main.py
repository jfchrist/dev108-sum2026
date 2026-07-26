# Placeholder for Madlibs main.py file

print("* * * Mad Libs Imitation Story Time! * * *\n")

#first would you like to play
playing = input("Would you like to play? [y/n]: ")

#initialize count for stories
count = 0

if playing.lower() == "y":
    #get and define player name
    playerName = input("\nYay! What is your name?: ")

    while playing.lower() == "y":
        print(f"\nAlright {playerName.capitalize()}, which setting would you like?")
        print("\n1. Fantasy Landscape\n2. Modern Cityscape")
        #get choice for story
        setting = input("\n1 or 2?: ")
        if setting.isdigit():

            if setting == "1":
                #inputs for story
                print(f"Alright! Let's get this started with some information from you!")
                inputOne = input("\n1) Write a type of medival building: ")
                inputTwo = input("\n2) A medival job occupation?: ")
                inputThree = input("\n3) Something you like: ")
                inputFour = input("\n4) A type of animal: ")
                inputFive = input("\n5) A royal title: ").capitalize()
                inputSix = input("\n6) An object: ")

                #output story
                print(f"\nOnce there was a {inputOne}. Inside lived a/an {inputTwo}. This {inputTwo} worked during the day as a/an {inputTwo} who liked {inputThree}, ")
                print(f"but they were secretly a/an {inputFour.capitalize()} Slayer! One day, the {inputFive} was kidnapped by a giant {inputFour}. The {inputFour} slaying {inputTwo} ")
                print(f"went on a journey and slew the giant {inputFour}! As a reward, they recieved a massive amount of {inputSix}s.\nTHE END")
                count += 1
                while True:
                    print(f"\nStories created: {count}")
                    playing = input("\nWould you like to play again? [y/n]: ")
                    if playing != "n" and playing != "y":
                        print("**Invalid input. Please try again.**")
                        continue
                    else:
                        break

            elif setting == "2":
                print(f"Alright! Let's get this started with some information from you!")
                #inputs for story (and validate)
                while True:
                    inputOne = input("\n1) A place to be (not home): ")
                    if inputOne.lower() != "home":
                        break
                    else:
                        print("Please read instructions carefully. Try again.")
                        continue
                inputTwo = input("\n2) An adjective: ")
                inputThree = input("\n3) An exotic animal: ")
                inputFour = input("\n4) A verb ending in 'ing': ")
                inputFive = input("\n5) A type of plant: ")
                while True:
                    inputSix = input("\n6) A number from 1 to 12: ")
                    if inputSix.isdigit():
                        inputSix = int(inputSix)
                        if inputSix >=1 and inputSix <=12:
                            break
                        else:
                            print("**Invalid input. Please try again.**")
                            continue
                    else:
                        print("**Invalid input. Please try again.**")
                        continue

                #output story
                print(f"\nSam was walking home from the {inputOne}. As he passed the {inputTwo} park, he saw a/an {inputThree} run into the park!")
                print(f"He chased after the {inputThree}, and he was shocked to see it {inputFour} through the {inputFive}!")
                print(f"Then, all of a sudden, Sam woke with a jolt from his dream. He checked his clock to see it was {inputSix} am.\nTHE END")
                count += 1
                while True:
                    print(f"\nStories created: {count}")
                    playing = input("\nWould you like to play again? [y/n]: ")
                    if playing != "n" and playing != "y":
                        print("**Invalid input. Please try again.**")
                        continue
                    else:
                        break

            else:
                print("**Invalid input. Please try again.**")
                continue

        else:
             print("**Invalid input. Please try again.**")
             continue
    else:
        print("\nThanks for playing! Enjoy your day!👋")
else:
    if playing.lower() == "n":
        print("\nOkay, enjoy the rest of your day!👋")
    else:
        print("**Sorry, program cannot process that information, try again?**")