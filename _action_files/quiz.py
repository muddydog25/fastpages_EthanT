YesNo = input(print("You are about to take an awesome quiz. Ready? (Yes or No)"))

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

questions = 3
correct = 0 

print('Greetings, ' + getpass.getuser() + " running " + sys.executable)
print("There will be " + str(questions) + " questions asked.")   

rsp = q_and_a(YesNo)
if rsp == "Yes":  
    print(rsp + "Lets go!")
    correct += 0
    
else:
    exit()

rsp = q_and_a("How many states are in the United States of America?")

if rsp == "50":
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

rsp = q_and_a("Which was the first dynasty to rule Imperial China?")

if rsp == "Qin Dynasty":
    
    print(" correct! ")
    correct += 1

elif rsp == "The Qin Dynasty":
    correct += 1

elif rsp == "Qin":
    correct += 1

else:
        print(rsp + " incorrect :( ")

if correct == 3:
    print("Congrats! " + (getpass.getuser() + " You got " + str(correct) +"/" + str(questions)))

elif correct == 2:
    print("Not bad, keep working! " + (getpass.getuser() + " You got " + str(correct) +"/" + str(questions)))

else:
    print((getpass.getuser() + " You got " + str(correct) +"/" + str(questions)) + " Its okay, better luck next time! ")



