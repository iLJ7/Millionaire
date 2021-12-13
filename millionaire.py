#!/usr/bin/env python3

import sys
import time
import random

with open("easy.txt") as e, open("medium.txt") as m, open("hard.txt") as h, open("final.txt") as f:
    easy_contents = e.readlines()
    medium_contents = m.readlines()
    hard_contents = h.readlines()
    final_contents = f.readlines()

with open("easy-answers.txt") as ea, open("medium-answers.txt") as ma, open("hard-answers.txt") as ha, open("final-answers.txt") as fa:
    easy_answers = ea.readlines()
    medium_answers = ma.readlines()
    hard_answers = ha.readlines()
    final_answers = fa.readlines()

welcome_msg = " Welcome to Who Wants to be a Millionaire! "

for i in range(10):
    print("-" * i + " " * len(welcome_msg) + "-" * i)

print("-" * 10 + welcome_msg + "-" * 10)

for i in range(9, 0, -1):
    print("-" * i + " " * + len(welcome_msg) + "-" * i)

time.sleep(1)

print()

print('For each question that follows, enter A, B, C or D for your answer respectively.')
time.sleep(5)
print('For each question, please wait for all 4 options to be displayed.')
time.sleep(5)

cash = ['100', '200', '300', '500', '1,000', '2,000', '4,000', '8,000', '16,000', '32,000',
       '64,000', '125,000', '250,000', '500,000', '1,000,000']

cash_int = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000,
            64000, 125000, 250000, 500000, 1000000]

maps = {
}

i = 0
while i < 10:

    maps[easy_contents[i].strip()] = easy_answers[i].split(',')
    maps[medium_contents[i].strip()] = medium_answers[i].split(',')
    maps[hard_contents[i].strip()] = hard_answers[i].split(',')

    i = i + 1

i = 0
while i < 3:

    maps[final_contents[i].strip()] = final_answers[i].split(',')

    i = i + 1

print()
i = 0
victory = 0

seen = []
fail = 0

while i < len(cash):
    print("For ??{cash}".format(cash = cash[i]) + " " * 10)

    if cash_int[i] <= 500:

        choice = random.choice([q for q in easy_contents if q not in seen])
        seen.append(choice)

    elif cash_int[i] <= 8000:

        choice = random.choice([q for q in medium_contents if q not in seen])
        seen.append(choice)

    elif cash_int[i] <= 125000:

        choice = random.choice([q for q in hard_contents if q not in seen])
        seen.append(choice)

    elif cash_int[i] > 125000:

        choice = random.choice([q for q in final_contents if q not in seen])
        seen.append(choice)

    print(choice)

    time.sleep(3)

    selection = [answer.strip() for answer in maps[choice.strip()]]
    correct_answer = selection[0].strip()

    letters = 'ABCD'
    dict = {}

    random.shuffle(selection)

    for j in range(0, 4):
        time.sleep(1)
        print(letters[j] + ": " + selection[j])
        dict[letters[j]] = selection[j]

    s = input('Answer: ')

    try:
        answer = dict[s.upper()]

    except:
        print('Error: Please enter A, B, C or D.')
        s = input('Answer: ')
        answer = dict[s.upper()]

    if answer == maps[choice.strip()][0] and i == len(cash) - 1:
        print("Incredible - you've won! You're going home with ??1,000,000!")

    elif answer == maps[choice.strip()][0] and i != len(cash) - 1:
        print("Correct! You're on ??{cash}".format(cash = cash[i]))

    elif i == 0:
        print("Incorrect!\nBetter luck next time, you're going home empty handed.")
        i = len(cash)

    else:
        print("Incorrect!\nYou're going home with ??{cash}.".format(cash = cash[i - 1]))
        i = len(cash)

    time.sleep(1.8)

    print()

    if i == len(cash):
        print('Thanks for playing.')

    i = i + 1
