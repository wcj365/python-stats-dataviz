import random

questions_cnt = 10
max_trials = 3


questions_list = []

for i in range(questions_cnt):

    a = random.randint(1, 10)
    b = random.randint(1, 10)

    pair = (a, b) if a >= b else (b, a)  # avoid negative result

    if pair in questions_list:
        continue                    # avoid duplicate questions
    else:
        questions_list.append(pair)

    for j in range(max_trials):

        answer = input("{} - {} = ".format(pair[0], pair[1]))
        
        try:
            answer = int(answer)
        except:
            print("try again.")
            continue

        if answer == pair[0] - pair[1]:
            print("good job!")
            break
        else:
            print("try again.")

        
print(questions_list)

