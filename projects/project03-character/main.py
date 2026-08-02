#Jaine Christ
#8/1/2026
#Project 03 - Character Generator
#Dev 108

import random

dire_wolf = [6,15,18,3,12,7]

#generate random ability score 1-20
def gen_ability_score():
    score = random.randint(1,20)
    return score

#function to pick random class
def gen_class():
    cClass = ["paladin 🛡️","rogue 🗡️","wizard 🧙","warlock 🔮","barbarian 🪓","artificer 🔥","fighter ⚔️","cleric 🕊️","druid 🍃", "monk 🙏"]
    choice = random.choice(cClass)
    return choice

#function to pick random race
def gen_race():
    race = ['human','dragonborn','elf','halforc','faerie','giant','gnome','halfling','dwarf']
    choice = random.choice(race)
    return choice

#function to demonstrate mock battle
def battle(dex,strength,name,con,):
        print("""Dire Wolf Stats:
    Strength:\t6
    Dexterity:\t15
    Health:\t\t18\n""")
        if dire_wolf[1] > dex:
            print("The wolf strikes first!")
            print(f"{name}'s Health:\t{con-dire_wolf[0]}")
            if con - dire_wolf[0] <= 0:
                print(f"{name} has lost. Better luck next time!")
            else:
                print(f"\nNow is {name}'s chance...")
                print(f"Dire Wolf's Health: {dire_wolf[2] - strength}")
                if dire_wolf[2] - strength <= 0:
                    print(f"{name} has defeated the dire wolf!")
                else:
                    print(f"\nThe injured Dire Wolf flees back to the woods. Perhaps {name} should take this as a victory...")
        else:
            print(f"{name} strikes first!")
            print(f"Dire Wolf's Health: {dire_wolf[2] - strength}")
            if dire_wolf[2] - strength <= 0:
                print(f"{name} has defeated the dire wolf!")
            else:
                print(f"\nThe wolf bites back!")
                print(f"{name}'s Health:\t{con-dire_wolf[0]}")
                if con - dire_wolf[0] <= 0:
                    print(f"{name} has lost. Better luck next time!")
                else:
                    print(f"\nThe injured Dire Wolf flees back to the woods. Perhaps {name} should take this as a victory...")

def main():
    #title
    print("* * * * Random Character Generator * * * *")
    print("\tver Quicker than rolling a d20")

    #intital question to start program
    start = input("\nWould you like to generate a random character?[y/n]:\t")
    if start == "y": 
        #initialize loop
        loop = "y"  
        #loop for multiple characters
        while loop == "y":
            name = input("\nWhat should we name your character?:\t").capitalize()

            #program runs for character's specs
            cClass = gen_class()
            race = gen_race()
            strength = gen_ability_score()
            dex = gen_ability_score()
            con = gen_ability_score()
            intel = gen_ability_score()
            wis = gen_ability_score()
            char = gen_ability_score()
            
            #program outputs specs
            print("* * * " * 4)
            print(f"Character Name: {name}\n")
            print(f"Class: {cClass.capitalize()}")
            print(f"Race: {race.capitalize()}\n")
            print(f"Strength:\t{strength}\nDexterity:\t{dex}\nConstitution:\t{con}\nIntelligence:\t{intel}\nWisdom:\t\t{wis}\nCharisma:\t{char}")
            print("* * * " * 4)

            #ask user if they would like to battle
            fight = input("\nWould you like to battle a beast?[y/n]:\t").lower()
            if fight =="y":
                print("\t* * * To Battle! * * *\n")
                print(f"\t{name} vs Dire Wolf\n")
                battle(dex,strength,name,con)
            else:
                print("Alrighty then\n")

            #loop for another character
            while True:
                print("* * * " * 4)
                loop = input("\nWould you like to create another character?[y/n]:\t").lower()
                if loop =="y":
                    break
                elif loop == "n":
                    break
                else:
                    print("* * Invalid Input, Please Try Again * *")
                    continue
        #end of loop
        else:
            if loop == "n":
                print("\n* * Good-bye! * *")
            else:
                print("**Invalid answer, please try again**\n")
        #initial question failure
    else:
        print("**Invalid answer, please try again**")

main()
   