
total = 0

while total < 100:
    num = int(input("Skriv inn et tall"))
    if num == -1:
        break
    total += num
    print("Current total:", total)

print("Hade bra")