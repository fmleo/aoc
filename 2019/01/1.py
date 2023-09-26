from math import *

total = 0

while True:
    try:
        mass = int(input())
        mass = floor(mass/3)
        mass = mass - 2

        total += floor(int(input()) / 3) - 2
    except EOFError:
        print(total)
        break