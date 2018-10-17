import random

def letter_difference(letter_a, letter_b):
    return abs(ord(letter_b) - ord(letter_a))


def word_difference(word1, word2):
    total_diff = 0

    for i in range(len(word1)):
        diff = letter_difference(word1[i], word2[i])
        total_diff += diff

    return total_diff


def print_sorted_word(word):
    print(sorted(word))


def change_vocals(word):
    vocals = ['a', 'e', 'i', 'o', 'u']
    new_word = ''

    for char in word:
        if char in vocals:
            new_word += random.choice(vocals)
        else:
            new_word += char
    return new_word


print(change_vocals("Jeg heter Ole-Magnus"))
