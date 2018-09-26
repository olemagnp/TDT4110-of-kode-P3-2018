import random


def roll():
    return random.randint(1, 6)


def get_points(guess, d1, d2, d3, d4, d5, d6):
    total = d1 + d2 + d3 + d4 + d5 + d6
    print("Faktisk rullet:", total)
    if guess == total:
        return 3
    elif abs(guess - total) <= 5:
        return 1
    else:
        return 0


def play_round():
    guess = int(input("Gjett på hva du kommer til å rulle: "))
    d1 = roll()
    d2 = roll()
    d3 = roll()
    d4 = roll()
    d5 = roll()
    d6 = roll()

    points = get_points(guess, d1, d2, d3, d4, d5, d6)
    print("Poeng for runde:", points)
    return points


total_points = 0
for i in range(4):
    total_points += play_round()

print("Du fikk", total_points, "poeng")