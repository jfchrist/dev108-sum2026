# starting Guess the Number program from our textbook

import random

#ask for and define player name
playerName = input("Hello, Player! What is your first name?: ")

def display_title():
    print("Guess the number!")
    print()

#ask what difficulty player wants
def ask_difficulty():
    while True:
        answer = input("Okay, "+ playerName+ ". What difficulty would you like to play? [easy/medium/hard]: ")
        print(answer)
        if answer.lower() == "easy" or answer.lower() == "medium" or answer.lower() == "hard":
            break
        else:
            print("Sorry, I didn't get that. Could you try again?")
            continue
    return answer.lower()

#run game on easy mode, range 1-10, limit 5 tries
def play_game_easy():
    #limit options from 1-10    
    number = random.randint(1, 10)
    print(f"I'm thinking of a number from 1 to 10...\n")
    count = 1

    while (guess := int(input("Your guess: "))) != number:
        if guess < number:
            print("Too low. Try again!")
            count += 1
        elif guess > number:
            print("Too high. Try again!")
            count += 1
    print(f"Good job! You guessed it in {count} tries!\n")

#run game on medium difficulty, rang 1-100, limit 8 tries
def play_game_medium():    
    number = random.randint(1, 100)
    print(f"I'm thinking of a number from 1 to 100...\n")
    count = 1

    while (guess := int(input("Your guess: "))) != number:
        if guess < number:
            print("Too low. Try again!")
            count += 1
        elif guess > number:
            print("Too high. Try again!")
            count += 1
    print(f"Good job! You guessed it in {count} tries!\n")

#run game on hard difficulty, range 1-1000, limit 10 tries
def play_game_hard():    
    number = random.randint(1, 1000)
    print(f"I'm thinking of a number from 1 to 1000...\n")
    count = 1

    while (guess := int(input("Your guess: "))) != number:
        if guess < number:
            print("Too low. Try again!")
            count += 1
        elif guess > number:
            print("Too high. Try again!")
            count += 1
    print(f"Good job! You guessed it in {count} tries!\n")
     
def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        difficulty = ask_difficulty()
        print()
        if difficulty == "easy":
            play_game_easy()
        elif difficulty == "medium":
            play_game_medium()
        elif difficulty == "hard":
            play_game_hard()
        again = input("Would you like to play again? (y/n): ")
        print()
    print(f"Thanks for playing, {playerName}! Good-Bye!")

# if started as the main module, call the main function

if __name__ == "__main__":
    main()
