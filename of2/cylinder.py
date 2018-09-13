import math

r = float(input("Radius: "))
h = float(input("Høyde: "))

V = h * math.pi * r ** 2

rounded = round(V, 5)

print("Volum:", rounded)
