
def input_int(text):
    num = input(text)

    while not num.isnumeric():
        print("Dette er ikke et tall")
        num = input(text)

    return int(num)


age = input_int("Skriv inn alderen din: ")

siblings = input_int("Hvor mange søsken har du? ")

print("Du er", age, "år og har", siblings, "søsken")
