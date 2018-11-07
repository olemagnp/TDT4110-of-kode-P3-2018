

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def binom(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print(binom(10, 4))