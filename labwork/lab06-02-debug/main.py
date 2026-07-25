# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
        test_score = float(test_score)
        score_total += test_score
        counter += 1
    else:
        break
    if test_score >= 0 and test_score <= 100:
        continue
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print("Total Score:", score_total,
      "\nAverage Score:", average_score)
print()
print("Bye")

#Test Case Values
#Test Number    Inputs      Expected Outputs    Actual Outputs  Pass/Fail
# 1             100, 90, 80     270, 90             270, 45       Fail
# ** Changed: moved erased second counter += 1 and moved adding total plus score to same first 'if' statement
# 2             100, 90, 80     270, 90             270, 90       Pass
# 3             100, 98, 80     278, 93             278, 93       Pass
# 4             100, 90.5, 95   285.5, 95.2         ERROR         Fail
# ** Changed: system to recognize tes_score variable as float not int
# 5             100, 90.5, 95   285.5, 95.2         285.5, 95
#
