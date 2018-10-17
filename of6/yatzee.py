import random


def roll_dice():
    return [random.randint(1, 6) for i in range(5)]


def change_die(dice, indices):
    for i in indices:
        dice[i] = random.randint(1, 6)


dice_list = roll_dice()
print(dice_list)
change_die(dice_list, [0, 2, 4])
print(dice_list)
