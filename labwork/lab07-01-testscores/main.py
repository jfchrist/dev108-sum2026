# Starting file for Exercise 6.1 in our textbook

#imported statistics module per your video--very helpful!
import statistics

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        elif score.isdigit():
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")
        else:
            print("Test score must be valid integer. Please try again.")

def process_scores(scores):
    total_scores = 0
    for i in scores:
        total_scores += i

    #calculate average
    average_score = round(total_scores/len(scores))

    #calculate median
    median = statistics.median(scores)

    # format and display the result
    print()
    print("Score total:       ", total_scores)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average_score)
    print("Lowest Score:      ", min(scores))
    print("Highest Score:     ", max(scores))
    print("Median Score:      ", median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Good-Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
