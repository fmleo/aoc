from math import *

total = 0

def calc(_mass: int) -> int:
    fuel = floor(_mass/3) - 2
    
    return fuel + calc(fuel) if fuel > 0 else 0

while True:
    try:
        mass = int(input())
        total += calc(mass)

    except EOFError:
        print(total)
        break