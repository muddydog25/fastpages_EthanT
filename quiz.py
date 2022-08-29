# Importing getpass, system, and random
import getpass, sys
import random

# Function to layout the questions and answers 
def ask_question (question, answer):

# Allow the answers to be typed in through input
    ans = input(question)
    print(ans)

# Print "Correct!"" and add 1 point (through return) per correct answer 
    if ans == answer:
        print("Correct!")
        return 1

# Print "Wrong" when an answer is incorrect and return 0 points
    else:
        print("Wrong")
        return 0

# A list of my questions and answers using the previously added "ask_question" function
question_list = ["Who was the first emperor of Imperial China?" , "What is 5 x 8?" , "How many states are there in the United States of America?" , "What command is used to include other functions that were previously developed?" , "What command is used to evaluate correct or incorrect response in this example?" , "Each 'if' command contains an '_________' to determine a true or false condition?"]
answer_list = ["Qin", "40", "50" , "import" , "if" , "expression"]

# Set points to 0 at the start of the quiz
points = 0

# If the length of the quiz is greater than 0, then random questions will be chosen from the "question_list" set
while len(question_list) > 0:
    index = random.randint(0, len(question_list) - 1)
    
# The points system where a point is rewarded for each correct answer    
    points = points + ask_question(question_list[index], answer_list[index])
    
# If a question or answer has already been used, then it shall be deleted    
    del question_list[index]
    del answer_list[index]

# Calculating score using the points system and dividing it by the total number of questions (6)
score = (points / 6)

# Calculating the percentage of correct answers by multiplying the score by 100
percent = (score * 100)

# Printing the percentage, and formatting the percentage in a way where two decimals can be shown (through "{:.2f}")
print("{:.2f}".format(percent) + "%")

# Adding final remarks based upon the users given scores
if points <= 5:
         print("Your total score is: ", points, "out of 6. Congratulations!")

elif points == 4:
         print("Your total score is: ", points, "out of 6. Not bad, keep working! " )

else:
         print("Your total score is: ", points, "out of 6. Its okay, better luck next time!")