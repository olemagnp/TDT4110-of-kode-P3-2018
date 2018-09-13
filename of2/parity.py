
tall = int(input("Tall: "))

is_even = tall % 2 == 0
print(is_even)

if is_even:
    print("Dette er et partall")
else:
    print("Dette er et oddetall")