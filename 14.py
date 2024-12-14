#!/usr/bin/python3
import math
import numpy as np
import time

start_time = time.time()

DAY = '14'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

if TEST:
    numTilesX = 11
    numTilesY = 7
else:
    numTilesX = 101
    numTilesY = 103


def generateRobotsFromInput():
    robots = []
    for line in lines:
        posStr = line.split()[0].split(",")
        pos = (int(posStr[0][2:]), int(posStr[1]))
        velStr = line.split()[1].split(",")
        vel = (int(velStr[0][2:]), int(velStr[1]))
        robots.append([pos, vel])
    return robots


def printMap(robots):
    robotPositions = robotPositionTotals(robots)
    for row in range(numTilesY):
        rowStr = ""
        for col in range(numTilesX):
            if (col, row) in robotPositions:
                rowStr += str(robotPositions[(col, row)])
            else:
                rowStr += "."
        print(rowStr)


def robotPositionTotals(robots):
    robotPositions = dict()
    for robot in robots:
        pos = robot[0]
        if pos not in robotPositions:
            robotPositions.update({pos: 1})
        else:
            robotPositions[pos] += 1
    return robotPositions


# part 1
robots = generateRobotsFromInput()
for step in range(100):
    for robot in robots:
        robot[0] = ((robot[0][0] + robot[1][0]) % numTilesX, (robot[0][1] + robot[1][1]) % numTilesY)

robotPositions = robotPositionTotals(robots)
quadrantTotals = []
runningSum = 0
for col in range(numTilesX // 2):
    for row in range(numTilesY // 2):
        if (col, row) in robotPositions:
            runningSum += robotPositions[(col, row)]
quadrantTotals.append(runningSum)

runningSum = 0
for col in range(numTilesX // 2):
    for row in range(numTilesY // 2 + 1, numTilesY):
        if (col, row) in robotPositions:
            runningSum += robotPositions[(col, row)]
quadrantTotals.append(runningSum)

runningSum = 0
for col in range(numTilesX // 2 + 1, numTilesX):
    for row in range(numTilesY // 2):
        if (col, row) in robotPositions:
            runningSum += robotPositions[(col, row)]
quadrantTotals.append(runningSum)

runningSum = 0
for col in range(numTilesX // 2 + 1, numTilesX):
    for row in range(numTilesY // 2 + 1, numTilesY):
        if (col, row) in robotPositions:
            runningSum += robotPositions[(col, row)]
quadrantTotals.append(runningSum)

print("Part 1 answer:", math.prod(quadrantTotals))


def checkForChristmasTree(robots):  # look for a number of rows of contiguous robots
    robotPositions = robotPositionTotals(robots)
    numPossibleRows = 0
    for row in range(numTilesY):
        positionInRow = []
        for col in range(numTilesX):
            if (col, row) in robotPositions:
                positionInRow.append(col)
        positionInRow.sort()
        numRobots = len(positionInRow)
        numAdjacent = np.sum(np.diff(positionInRow) == 1)
        if numAdjacent > 10 and numAdjacent / numRobots > 0.7:  # more than 10 robots are adjacent to each other and they constitute more than 70% of the robots in this row
            numPossibleRows += 1
    if numPossibleRows > 5:  # if there more than 5 rows of largely adjacent robots, they're likely making a picture...
        return True
    return False


# part 2
robots = generateRobotsFromInput()
step = 0
while True:
    for robot in robots:
        robot[0] = ((robot[0][0] + robot[1][0]) % numTilesX, (robot[0][1] + robot[1][1]) % numTilesY)
    step += 1
    if checkForChristmasTree(robots):
        break
print("Part 2 answer:", step)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
