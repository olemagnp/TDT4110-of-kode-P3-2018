import random


def roll_dice():
    return [random.randint(1, 6) for i in range(5)]


def roll_dice_manual():
    dice = []
    for i in range(5):
        dice.append(random.randint(1, 6))
    return dice


def num_with_vals(dice, value):
    total = 0
    for die in dice:
        if die == value:
            total += 1
    return total


def points_before_bonus():
    total_points = 0
    for i in range(1, 7):
        dice = roll_dice()
        points = i * num_with_vals(dice, i)
        total_points += points
    return total_points


print(points_before_bonus())