#!/usr/bin/python3
from collections import deque
import time

start_time = time.time()

DAY = '10'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

NEXTPOS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

map = [[int(x) for x in row] for row in lines]
numRows = len(map)
numCols = len(map[0])

# part 1
trailheadScores = 0
for row in range(numRows):
    for col in range(numCols):
        if map[row][col] == 0:
            nextSteps = deque([(row, col)])
            visited = set()
            while nextSteps:
                r, c = nextSteps.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                if map[r][c] == 9:
                    trailheadScores += 1
                for rowDelta, colDelta in NEXTPOS:
                    nextRow, nextCol = r + rowDelta, c + colDelta
                    if 0 <= nextRow < numRows and 0 <= nextCol < numCols and map[nextRow][nextCol] == map[r][c] + 1:
                        nextSteps.append((nextRow, nextCol))
print("Part 1 answer:", trailheadScores)


def followTrails(row, col, routeCount):
    if map[row][col] == 9:
        return 1
    if (row, col) in routeCount:
        return routeCount[(row, col)]
    numRoutes = 0
    for rowDelta, colDelta in NEXTPOS:
        nextRow, nextCol = row + rowDelta, col + colDelta
        if 0 <= nextRow < numRows and 0 <= nextCol < numCols and map[nextRow][nextCol] == map[row][col] + 1:
            numRoutes += followTrails(nextRow, nextCol, routeCount)
    routeCount[(row, col)] = numRoutes
    return numRoutes


# part 2
trailheadRatings = 0
for row in range(numRows):
    for col in range(numCols):
        if map[row][col] == 0:
            trailheadRatings += followTrails(row, col, {})
print("Part 2 answer:", trailheadRatings)

print("Completed in %.1f seconds" % (time.time() - start_time))
