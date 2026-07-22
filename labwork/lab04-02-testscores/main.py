# starting file for Exercise 3-2

# be sure to follow along with my video demonstration video in our Canvas assignment instructions if you need help

# display a welcome message
print("The Test Scores Calculator")
print()
print("Enter test scores")
print("Enter 'end' to end input")
print("======================")


while True:
    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0
    while True:
        test_score = input("Enter test score: ")
        if test_score == "end":
            break
        else:
            test_score = int(test_score)
            if test_score >= 0 and test_score <= 100:
                score_total += test_score
                counter += 1
            else:
                print("Test score must be from 0 through 100. Score discarded. Try again.")
                continue

    # calculate average score and validate
    if score_total == 0 or counter == 0:
        print("Sorry, the Program needs at least one valid score to operate.")
        continue
    else:
        average_score = round(score_total / counter)
                    
    # format and display the result
    print("======================")
    print("Total Score:", score_total,
        "\nAverage Score:", average_score)
    
    # ask user if they would like to input again
    print("======================")
    answer = input("Would you like to input more test scores? y/n?: ")
    if answer.lower() == "y":
        continue
    else:
        break
print()
print("Good-Bye!")
