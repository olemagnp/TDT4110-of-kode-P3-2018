
goal = 42
user_input = int(input("Gjett et tall: "))

while user_input != goal:
    if user_input > goal:
        print("Du gjetter for høyt")
    else:
        print("Du gjetter for lavt")
    user_input = int(input("Gjett et tall: "))

print("Du gjettet riktig")
