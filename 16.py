#!/usr/bin/python3
import math
import sys
import heapq
import time

start_time = time.time()

DAY = '16'
TEST = True
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

sys.setrecursionlimit(10 ** 6)

UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

numRows = len(lines)
numCols = len(lines[0])

START = (numRows - 2, 1)
END = (1, numCols - 2)

print(START, "to", END)


def exploreMapRecursively(score, row, col, dirIndex, visited):
    if (row, col) in visited or lines[row][col] == "#":
        return math.inf
    straightOn = dirIndex
    turnLeft = (dirIndex + 3) % 4
    turnRight = (dirIndex + 1) % 4
    visited.append((row, col))
    if lines[row][col] == "E":
        return score
    else:
        return min(exploreMapRecursively(score + 1, row + DIRECTIONS[straightOn][0], col + DIRECTIONS[straightOn][1], straightOn, visited.copy()),
                   exploreMapRecursively(score + 1001, row + DIRECTIONS[turnLeft][0], col + DIRECTIONS[turnLeft][1], turnLeft, visited.copy()),
                   exploreMapRecursively(score + 1001, row + DIRECTIONS[turnRight][0], col + DIRECTIONS[turnRight][1], turnRight, visited.copy()))


def exploreMapHeap(startingRow, startingCol, startingDirIndex):
    stillToProcess = []
    visited = set()
    heapq.heappush(stillToProcess, (0, startingRow, startingCol, startingDirIndex))
    while stillToProcess:
        score, row, col, dirIndex = heapq.heappop(stillToProcess)
        if (row, col) in visited or lines[row][col] == "#":
            continue
        if lines[row][col] == "E":
            return score
        visited.add((row, col))
        straightOn = dirIndex
        turnLeft = (dirIndex + 3) % 4
        turnRight = (dirIndex + 1) % 4
        heapq.heappush(stillToProcess, (score + 1, row + DIRECTIONS[straightOn][0], col + DIRECTIONS[straightOn][1], straightOn))
        heapq.heappush(stillToProcess, (score + 1001, row + DIRECTIONS[turnLeft][0], col + DIRECTIONS[turnLeft][1], turnLeft))
        heapq.heappush(stillToProcess, (score + 1001, row + DIRECTIONS[turnRight][0], col + DIRECTIONS[turnRight][1], turnRight))


def exploreMapHeapPart2(startingRow, startingCol, startingDirIndex):
    wholeRoutes = []
    stillToProcess = []
    heapq.heappush(stillToProcess, (0, startingRow, startingCol, startingDirIndex, set()))
    while stillToProcess:
        score, row, col, dirIndex, route = heapq.heappop(stillToProcess)
        if (row, col) in route or lines[row][col] == "#":
            continue
        route.add((row, col))
        if lines[row][col] == "E":
            wholeRoutes.append((score, route))
            continue
        straightOn = dirIndex
        turnLeft = (dirIndex + 3) % 4
        turnRight = (dirIndex + 1) % 4
        heapq.heappush(stillToProcess, (score + 1, row + DIRECTIONS[straightOn][0], col + DIRECTIONS[straightOn][1], straightOn, route.copy()))
        heapq.heappush(stillToProcess, (score + 1001, row + DIRECTIONS[turnLeft][0], col + DIRECTIONS[turnLeft][1], turnLeft, route.copy()))
        heapq.heappush(stillToProcess, (score + 1001, row + DIRECTIONS[turnRight][0], col + DIRECTIONS[turnRight][1], turnRight, route.copy()))

    lowestScore = math.inf
    for route in wholeRoutes:
        if route[0] < lowestScore:
            lowestScore = route[0]

    uniqueTiles = set()
    for route in wholeRoutes:
        if route[0] == lowestScore:
            uniqueTiles = uniqueTiles.union(set(route[1]))
    # print("Lowest score of", lowestScore, "and", len(uniqueTiles), "unique tiles")
    return len(uniqueTiles)


# part 1
# score = exploreMapRecursively(0, START[0], START[1], 1, [])   # The recursive version takes way too long to run on the real data...
score = exploreMapHeap(START[0], START[1], 1)
print("Part 1 answer:", score)

# part 2
numTiles = exploreMapHeapPart2(START[0], START[1], 1)  # This brute force exhaustive search version also takes way too long (memory runway) to run on the real data (works on the test data!)...
print("Part 2 answer:", numTiles)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
