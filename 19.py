#!/usr/bin/python3
import time

start_time = time.time()

DAY = '19'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

patterns = [x.strip() for x in lines[0].split(",")]


def checkDesignPossible(design):
    if design in cache:
        return cache[design]
    numWays = design in patterns
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            numWays += checkDesignPossible(design[len(pattern):])
    cache[design] = numWays
    return numWays


# parts 1 and 2
cache = {}
numPossibleDesigns = 0
numPossibleWays = 0
for design in lines[2:]:
    numWays = checkDesignPossible(design)
    numPossibleDesigns += numWays > 0
    numPossibleWays += numWays
print("Part 1 answer:", numPossibleDesigns)
print("Part 2 answer:", numPossibleWays)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
