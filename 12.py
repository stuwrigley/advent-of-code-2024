#!/usr/bin/python3
from collections import deque
import numpy as np
import time

start_time = time.time()

DAY = '12'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

NEXTPOS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

numRows = len(lines)
numCols = len(lines[0])

# part 1
pricePart1 = 0
pricePart2 = 0
visited = set()
for row in range(numRows):
    for col in range(numCols):
        if (row, col) in visited:
            continue
        locationsToCheck = deque([(row, col)])
        area = 0
        perimeter = 0
        regionSides = dict()
        while locationsToCheck:
            thisRow, thisCol = locationsToCheck.popleft()
            if (thisRow, thisCol) in visited:
                continue
            visited.add((thisRow, thisCol))
            area += 1
            for rowDelta, colDelta in NEXTPOS:
                nextRow, nextCol = thisRow + rowDelta, thisCol + colDelta
                if 0 <= nextRow < numRows and 0 <= nextCol < numCols and lines[nextRow][nextCol] == lines[thisRow][thisCol]:  # adjacent plot is same plant
                    locationsToCheck.append((nextRow, nextCol))
                else:  # adjacent plot is not the same plant, so it's a perimeter
                    perimeter += 1
                    if (rowDelta, colDelta) not in regionSides:
                        regionSides[(rowDelta, colDelta)] = set()
                    regionSides[(rowDelta, colDelta)].add((thisRow, thisCol))
        pricePart1 += area * perimeter

        # do part 2
        numSides = 0
        for rowDelta, colDelta in NEXTPOS:  # consider each edge type in turn (left, right, top, bottom)
            if rowDelta != 0:  # tops and bottoms
                rows = set([x[0] for x in regionSides[(rowDelta, colDelta)]])  # all the unique map rows
                for r in rows:
                    cols = []
                    for s in regionSides[(rowDelta, colDelta)]:
                        if s[0] == r:
                            cols.append(s[1])
                    cols.sort()
                    numSides += 1 + sum(abs(np.diff(cols)) > 1)  # count the number of discontinuities
            if colDelta != 0:  # lefts and rights
                cols = set([x[1] for x in regionSides[(rowDelta, colDelta)]])  # all the unique map cols
                for c in cols:
                    rows = []
                    for s in regionSides[(rowDelta, colDelta)]:
                        if s[1] == c:
                            rows.append(s[0])
                    rows.sort()
                    numSides += 1 + sum(abs(np.diff(rows)) > 1)  # count the number of discontinuities
        pricePart2 += area * numSides

print("Part 1 answer:", pricePart1)
print("Part 2 answer:", pricePart2)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
