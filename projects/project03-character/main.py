#Jaine Christ
#8/1/2026
#Project 03 - Character Generator
#Dev 108

import random

#dire wolf abilities
dire_wolf = [6,15,18,3,12,7]


#generate random ability score 1-20
def gen_ability_score():
    score = random.randint(1,20)
    return score

#function to pick random class
def gen_class():
    cClass = ["paladin 🛡️","rogue 🗡️","wizard 🧙","warlock 🔮",'sorcerer 🧙‍♂️',"barbarian 🪓","artificer 🔥","fighter ⚔️","cleric 🕊️","druid 🍃", "monk 🙏"]
    choice = random.choice(cClass)
    return choice

#function to pick random race
def gen_race():
    race = ['human','dragonborn','elf','halforc','faerie','giant','gnome','halfling','dwarf']
    choice = random.choice(race)
    return choice

#function to demonstrate mock battle
def battle(dex,strength,name,con,cClass):
    #initialize dire wolf health
    direHealth = 18
    print("""Dire Wolf Stats:
    Strength:\t6
    Dexterity:\t15
    Health:\t18""")
    #if wolf is faster
    if dire_wolf[1] > dex:
            while direHealth >= 0 and con >= 0:
                print("\nThe wolf strikes first!")
                con -= dire_wolf[0]
                print(f"{name}'s Health:\t{con}")

                #random heal chance, 25%
                if cClass == "cleric 🕊️" or cClass == 'paladin 🛡️':
                    chance = random.randint(0,3)
                    if chance == 1:
                        con += 6
                        print(f"\n{name} has healed themselves!")
                        print(f"{name}'s Health: {con}")
                    else:
                        pass
                else:
                    pass

                if con<= 0:
                    print(f"\n{name} has lost. Better luck next time!")
                    break
                else:
                    print(f"\nNow is {name}'s chance...they strike!")
                    direHealth -= strength
                    print(f"Dire Wolf's Health: {direHealth}")

                    #random fireball chance, 50%
                    if cClass == 'warlock 🔮' or cClass == 'sorcerer 🧙‍♂️' or cClass == 'wizard 🧙':
                        chance = random.randint(0,1)
                        if chance == 1:
                            direHealth -= 25
                            print(f"\n{name} casts a mighty fireball!")
                            print(f"Dire Wolf Health: {direHealth}")
                        else:
                            pass
                    else:
                        pass
                    if direHealth <= 0:
                        print(f"\n{name} has defeated the dire wolf!")
                        break
                    else:
                        continue
    #if character is faster
    else:
        while direHealth >= 0 and con >= 0:
            print(f"\n{name} strikes first!")
            direHealth -= strength
            print(f"Dire Wolf's Health: {direHealth}")
            #random fireball chance, 50%
            if cClass == 'warlock 🔮' or cClass == 'sorcerer 🧙‍♂️' or cClass == 'wizard 🧙':
                    chance = random.randint(0,1)
                    if chance == 1:
                        direHealth -= 25
                        print(f"\n{name} casts a mighty fireball!")
                        print(f"Dire Wolf Health: {direHealth}")
                    else:
                        pass
            else:
                    pass
            if direHealth <= 0:
                print(f"{name} has defeated the dire wolf!")
                break
            else:
                print(f"\nThe wolf bites back!")
                con-=dire_wolf[0]
                print(f"{name}'s Health:\t{con}")
                #random heal chance, 25%
                if cClass == "cleric 🕊️" or cClass == 'paladin 🛡️':
                    chance = random.randint(0,3)
                    if chance == 1:
                        con += 6
                        print(f"\n{name} has healed themselves!")
                        print(f"{name}'s Health: {con}")
                    else:
                        pass
                else:
                    pass
                if con<= 0:
                    print(f"\n{name} has lost. Better luck next time!")
                    break
                if con <= 0:
                    print(f"\n{name} has lost. Better luck next time!")
                    break
                else:
                    continue

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
            con = gen_ability_score() + 5
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
                battle(dex,strength,name,con,cClass)
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
   