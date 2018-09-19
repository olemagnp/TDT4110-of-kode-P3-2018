
limit = int(input("Hvor høyt skal summen gå? "))

total = 0
i = 1

while total <= limit:
    total = total + i
    if total <= limit:
        print(f"{total} + {i} = {total + i}")
        print(total, "+", i, "=", total + i)
    i += 1
