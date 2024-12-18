#!/usr/bin/python3
from collections import deque
import time

start_time = time.time()

DAY = '18'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

fallers = []
for line in lines:
    fallers.append((int(line.split(",")[1]), int(line.split(",")[0])))

UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

START = (0, 0)
if TEST:
    END = (6, 6)
    NUM_FALLERS = 12
else:
    END = (70, 70)
    NUM_FALLERS = 1024


def printMap(corrupted):
    for row in range(END[0] + 1):
        str = ""
        for col in range(END[1] + 1):
            if (row, col) in corrupted:
                str += "#"
            else:
                str += "."
        print(str)


def navigateMap(numFallers):
    stillToProcess = deque([(0, START[0], START[0])])
    visited = set()
    while stillToProcess:
        step, row, col = stillToProcess.popleft()
        if row == END[0] and col == END[1]:
            return step
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for rowDelta, colDelta in DIRECTIONS:
            nextRow = row + rowDelta
            nextCol = col + colDelta
            if 0 <= nextRow <= END[0] and 0 <= nextCol <= END[1] and (nextRow, nextCol) not in fallers[:numFallers]:
                stillToProcess.append((step + 1, nextRow, nextCol))  # add to queue
    return -1


# part 1
print("Part 1 answer:", navigateMap(NUM_FALLERS))

# part 2
for numFallers in range(NUM_FALLERS, len(fallers)):  # we know it's fine up to the part 1 number of fallers. This is still uncomfortably brute force style...
    if navigateMap(numFallers) == -1:
        print("Part 2 answer:", str(fallers[numFallers - 1][1]) + "," + str(fallers[numFallers - 1][0]))
        break

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
