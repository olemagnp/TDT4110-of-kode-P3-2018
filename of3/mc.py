import random

correct_counter = 0

for i in range(10):
    correct = random.randint(1, 4)
    guessed = int(input("Velg et svaralternativ: "))
    if guessed == correct:
        print("Det var riktig")
        correct_counter += 1
    else:
        print("Det var feil")

percentage_correct = correct_counter / 10 * 100
if percentage_correct > 40:
    print("Du besto, med", percentage_correct, "% riktig")
else:
    print("Du strøk, med", percentage_correct, "% riktig")
