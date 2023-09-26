from math import *

total = 0

while True:
    try:
        intcode = [int(i) for i in input().split(",")]
        intcode[1] = 12
        intcode[2] = 2

        for i in range(0, len(intcode), 4):
            match intcode[i]:
                case 1:
                    intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
                case 2:
                    intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
                case _:
                    break
        
        print(intcode[0])

    except EOFError:
        break