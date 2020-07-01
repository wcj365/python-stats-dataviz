#!/usr/bin/env python3

'''
This program can be used to generate simple arithmetic quizes for kids.
You can customize this program to suit the kids's level of math skills.
For example, change the maximum number of trials or the range of numbers.

You can also limit the kind of arithemetics. By default, the program randomly
pick from one of the four operations (add, subtract, multiple, divide) for each 
quiz. You can modify the question_list to limit the choices. 
'''

import random

quiz_cnt = 5                              # Total number of quizzes 
max_trials = 3                            # Maximum number of trials for a given quiz

start_int = 1                             # The minimum number used in the quiz
stop_int = 10                             # The maximum number used in the quiz

operation_list = ("+", "-", "*", "/")     # Remove elements to limit the choices

quiz_list = []                            # This holds the complete list of quizes
answer_list = []                          # This holds the complete list of quizes


print ("\n*** Math Quiz ***\n")

for i in range(quiz_cnt):
    
    operation = random.choice(operation_list)    # Randomly select one of the operations from the list

    while True:

        a = random.randint(start_int, stop_int)
        b = random.randint(start_int, stop_int)

        if (operation == "/") and (a % b != 0):  # Ensure the division can be performed
            continue

        if (operation == "-") and (a < b):       # Eliminate the possibility of negative answer
            quiz = (b, operation, a) 
        else:
            quiz = (a, operation, b) 

        if quiz not in quiz_list:
            break                    # avoid duplicate quizs


    for j in range(max_trials):

        while True:
            your_input = input("Quiz {} of {}: {} {} {} = ".format(i+1, quiz_cnt, quiz[0], quiz[1], quiz[2]))
        
            try:
                your_answer = int(your_input)
                break
            except:
                print("please enter a number.")
                continue

        if operation == "+":
            correct_answer = quiz[0] + quiz[2]
        elif operation == "-":
            correct_answer = quiz[0] - quiz[2]
        elif operation == "*":
            correct_answer = quiz[0] * quiz[2]
        elif operation == "/":
            correct_answer = int(quiz[0] / quiz[2])
        else:
            raise Exception('The system encountered a mysterious operation: {}'.format(operation))

        if your_answer == correct_answer:
            break
        else:
            print("please try again (attempt {} of {})".format(j+1, max_trials))

    quiz_list.append(quiz)
    answer_list.append((correct_answer, your_answer))

    print("")

        
print("\n*** Summary Report ***", end="\n\n")        
for i in range(quiz_cnt):
    print ("{} {} {} = {} {}"     \
        .format(quiz_list[i][0], quiz_list[i][1], quiz_list[i][2], answer_list[i][0],     \
                "" if answer_list[i][0] == answer_list[i][1] else ("(your answered: " + str(answer_list[i][1]) + ")")))

correct_cnt = len([x for x in answer_list if x[0] == x[1]])

print("\nYou got {} correct out of {} questions.\n".format(correct_cnt, quiz_cnt))
