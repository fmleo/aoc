from math import *

total = 0

while True:
    try:
        total += floor(int(input()) / 3) - 2
    except EOFError:
        print(total)
        break