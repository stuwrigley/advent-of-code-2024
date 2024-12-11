#!/usr/bin/python3
import time

start_time = time.time()

DAY = '11'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

stones = [int(x) for x in lines[0].split()]

# part 1
numBlinks = 25
for blink in range(numBlinks):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone)) % 2 == 0:
            stoneStr = str(stone)
            newStones.append(int(stoneStr[:len(stoneStr) // 2]))
            newStones.append(int(stoneStr[len(stoneStr) // 2:]))
        else:
            newStones.append(stone * 2024)
    stones = newStones
print("Part 1 answer:", len(stones))


def blinkAtSingleStone(stone, blinks):
    if (stone, blinks) in previousStoneStates:
        return previousStoneStates[(stone, blinks)]
    if blinks == 0:
        previousStoneStates[(stone, blinks)] = 1
    elif stone == 0:
        previousStoneStates[(stone, blinks)] = blinkAtSingleStone(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        stoneStr = str(stone)
        previousStoneStates[(stone, blinks)] = blinkAtSingleStone(int(stoneStr[:len(stoneStr) // 2]), blinks - 1) + blinkAtSingleStone(int(stoneStr[len(stoneStr) // 2:]), blinks - 1)
    else:
        previousStoneStates[(stone, blinks)] = blinkAtSingleStone(stone * 2024, blinks - 1)
    return previousStoneStates[(stone, blinks)]


# part 2
previousStoneStates = {}
numStones = 0
numBlinks = 75
stones = [int(x) for x in lines[0].split()]
for stone in stones:
    numStones += blinkAtSingleStone(stone, numBlinks)
print("Part 2 answer:", numStones)

print("Completed in %.1f seconds" % (time.time() - start_time))
