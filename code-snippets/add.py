import random

questions_cnt = 10
max_trials = 3

questions_list = []

for i in range(questions_cnt):

    a = random.randint(1, 10)
    b = random.randint(1, 10)


    if (a,b) in questions_list:
        continue                    # avoid duplicate questions
    else:
        questions_list.append((a,b))

    for j in range(max_trials):

        c = input("{} + {} = ".format(a, b))
        
        try:
            c = int(c)
        except:
            print("try again.")
            continue

        if c == a + b:
            print("good job!")
            break
        else:
            print("try again.")

        
print(questions_list)

