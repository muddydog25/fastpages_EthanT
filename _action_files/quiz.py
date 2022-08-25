def q_and_a(prompt):
    print("Question: ")
    student = input()
    print("Answer: ")

    q_and_a("test yes or no?")
    q_and_a("What is 8 x 5?")
    q_and_a("What is 50 / 5?")

import getpass, sys
from tkinter.messagebox import YES

def q_and_a(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 4
correct = 0



print('Greetings, ' + getpass.getuser() + " running " + sys.executable)
print("There will be " + str(questions) + " questions asked.")
q_and_a("Are you ready to take an awesome short quiz?")

rsp = q_and_a("Yes or No?")
if rsp == "Yes":
    print("Lets go!")

else:
    quit()



# rsp = response 

rsp = q_and_a("test yes or no?")

if rsp == "yes":
        print(rsp + " correct! ")
        correct += 1

else: 
        print(rsp + " incorrect :(")

rsp = q_and_a("What is 8 x 5?")

if rsp == "40":
        print(rsp + " correct! ")
        correct += 1

else: 
        print(rsp + " incorrect :(")



