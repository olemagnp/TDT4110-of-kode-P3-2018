import random


def answer_question(question):
    answer = random.choice(["Ja", "Nei"])
    print("Spm:", question)
    print("Svar:", answer)


while True:
    spm = input("Hva er spørsmålet ditt?")
    answer_question(spm)
