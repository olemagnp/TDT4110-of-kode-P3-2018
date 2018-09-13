
x = int(input("Tall: "))

if x in (2,3,5,7,11,13,17,19,23,29):
    print(x, "er et primtall <= 30")
elif x % 4 == 0:
    print(x, "/ 4 =", x/4)
elif x % 2 == 1:
    print(x, "er odde")
else:
    print(x, "/ 2 =", x/2)
    print(str(x) + " / 2 = " + str(x / 2))
