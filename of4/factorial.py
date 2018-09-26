
def factorial(x):
    product = 1
    for i in range(1, x + 1):
        product = product * i
    return product


y = factorial(12)
print("Fakultetet av 12 er", y)
