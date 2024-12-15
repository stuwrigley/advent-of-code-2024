#!/usr/bin/python3
import time

start_time = time.time()

DAY = '15'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

direction = {'>': RIGHT, '<': LEFT, '^': UP, 'v': DOWN}


def printMapPart1(walls, boxes, curPos):
    for row in range(numRows):
        s = ""
        for col in range(numCols):
            if curPos == (row, col):
                s += "@"
            elif (row, col) in walls:
                s += "#"
            elif (row, col) in boxes:
                s += "O"
            else:
                s += "."
        print(s)


def scoreMap(boxes):
    score = 0
    for box in boxes:
        score += box[0] * 100 + box[1]
    return score


def scoreMapPart2(boxes):
    score = 0
    for box in boxes:
        score += box[0][0] * 100 + box[0][1]
    return score


# part 1
walls = set()
boxes = set()
numCols = len(lines[0])
numRows = 0
movements = ""
currentPosition = (-1, -1)
for lineCount, line in enumerate(lines):
    if line == '':
        numRows = lineCount
        continue
    if line[0] == '#':
        for pos, char in enumerate(line):
            if char == "#":
                walls.add((lineCount, pos))
            if char == "O":
                boxes.add((lineCount, pos))
            if char == "@":
                currentPosition = (lineCount, pos)
    else:
        movements += line
for movement in movements:
    targetPosition = (currentPosition[0] + direction[movement][0], currentPosition[1] + direction[movement][1])
    if targetPosition not in boxes and targetPosition not in walls:
        currentPosition = targetPosition
    else:
        nextPosition = targetPosition
        while nextPosition not in walls:
            if nextPosition not in boxes and targetPosition not in walls:
                currentPosition = targetPosition
                boxes.remove(currentPosition)
                boxes.add(nextPosition)
                break
            nextPosition = (nextPosition[0] + direction[movement][0], nextPosition[1] + direction[movement][1])
print("Part 1 answer:", scoreMap(boxes))

# part 2
walls = set()
boxes = set()
numCols = len(lines[0] * 2)
numRows = 0
movements = ""
currentPosition = (-1, -1)
for lineCount, line in enumerate(lines):
    if line == '':
        numRows = lineCount
        continue
    if line[0] == '#':
        for pos, char in enumerate(line):
            if char == "#":
                walls.add((lineCount, pos * 2))
                walls.add((lineCount, pos * 2 + 1))
            if char == "O":
                boxes.add(((lineCount, pos * 2), (lineCount, pos * 2 + 1)))
            if char == "@":
                currentPosition = (lineCount, pos * 2)
    else:
        movements += line


def boxLeftEdges(boxes):
    leftEdges = set()
    for box in boxes:
        leftEdges.add(box[0])
    return leftEdges


def boxRightEdges(boxes):
    rightEdges = set()
    for box in boxes:
        rightEdges.add(box[1])
    return rightEdges


def printMapPart2(walls, boxes, curPos):
    leftEdges = boxLeftEdges(boxes)
    rightEdges = boxRightEdges(boxes)
    for row in range(numRows):
        s = ""
        for col in range(numCols):
            if curPos == (row, col):
                s += "@"
            elif (row, col) in walls:
                s += "#"
            elif (row, col) in leftEdges:
                s += "["
            elif (row, col) in rightEdges:
                s += "]"
            else:
                s += "."
        print(s)


def boxesBeyondOnRow(boxes, currentPosition, dir, limit):
    boxesBeyond = set()
    for box in boxes:
        if dir < 0:
            if box[0][0] == currentPosition[0] and box[0][1] < currentPosition[1] and box[0][1] > limit:
                boxesBeyond.add(box)
        else:
            if box[0][0] == currentPosition[0] and box[0][1] > currentPosition[1] and box[0][1] < limit:
                boxesBeyond.add(box)
    return boxesBeyond


def defNearestWallOnRow(walls, currentPosition, dir):
    nearestWallCol = 1
    if dir > 0:
        nearestWallCol = numCols - 2
    for wall in walls:
        if wall[0] == currentPosition[0]:
            if dir < 0:
                if nearestWallCol < wall[1] < currentPosition[1]:
                    nearestWallCol = wall[1]
            else:
                if currentPosition[1] < wall[1] < nearestWallCol:
                    nearestWallCol = wall[1]
    return nearestWallCol


def boxesOnNextRowAdjacentToCol(boxes, rowOfInterest, col):
    b = set()
    for box in boxes:
        if box[0][0] == rowOfInterest and (box[0][1] in col or box[1][1] in col):
            b.add(box)
    return b


def boxTouchingWall(box, dir):
    for wall in walls:
        if (box[0][0] + dir, box[0][1]) == wall or (box[1][0] + dir, box[1][1]) == wall:
            return True
    return False


for movement in movements:
    targetPosition = (currentPosition[0] + direction[movement][0], currentPosition[1] + direction[movement][1])
    leftEdges = boxLeftEdges(boxes)
    rightEdges = boxRightEdges(boxes)
    if targetPosition not in walls:
        if targetPosition not in leftEdges and targetPosition not in rightEdges:  # move into a free space
            currentPosition = targetPosition
        else:
            if direction[movement] == UP or direction[movement] == DOWN:
                boxesToMove = set()
                boxesToCheck = boxesOnNextRowAdjacentToCol(boxes, currentPosition[0] + direction[movement][0], [currentPosition[1]])
                canShuffle = True
                while boxesToCheck:
                    currentBox = boxesToCheck.pop()
                    if boxTouchingWall(currentBox, direction[movement][0]):
                        canShuffle = False
                        break
                    boxesToMove.add(currentBox)
                    boxesOnNextRow = boxesOnNextRowAdjacentToCol(boxes, currentBox[0][0] + direction[movement][0], [currentBox[0][1], currentBox[1][1]])
                    boxesToCheck = boxesToCheck.union(boxesOnNextRow)
                if canShuffle:
                    for box in boxesToMove:
                        boxes.remove(box)
                    for box in boxesToMove:
                        boxToAdd = ((box[0][0] + direction[movement][0], box[0][1]), (box[1][0] + direction[movement][0], box[1][1]))  # ((edgeToShuffle[0], edgeToShuffle[1] - 1), edgeToShuffle)
                        boxes.add(boxToAdd)
                    currentPosition = (currentPosition[0] + direction[movement][0], currentPosition[1])

            if direction[movement] == LEFT or direction[movement] == RIGHT:
                nearestWall = defNearestWallOnRow(walls, currentPosition, direction[movement][1])
                if targetPosition[1] == nearestWall:
                    continue

                shift = 2 * direction[movement][1]
                boxesBeyond = boxesBeyondOnRow(boxes, currentPosition, direction[movement][1], nearestWall)
                spaceToShuffle = True
                if direction[movement][1] < 1:
                    spaceToShuffle = (currentPosition[1] - nearestWall - 1) / 2 > len(boxesBeyond)
                else:
                    spaceToShuffle = (nearestWall - currentPosition[1] - 2) / 2 >= len(boxesBeyond)
                if spaceToShuffle:
                    boxesBeyondLeftEdges = boxLeftEdges(boxesBeyond)
                    nextPos = currentPosition[1] + shift
                    if direction[movement][1] > 0:
                        nextPos -= 1
                    edgesToShuffle = set()
                    while (currentPosition[0], nextPos) not in walls:
                        if (currentPosition[0], nextPos) in boxesBeyondLeftEdges:
                            edgesToShuffle.add((currentPosition[0], nextPos))
                        else:
                            break
                        nextPos += shift
                    if len(edgesToShuffle) > 0:
                        for edgeToShuffle in edgesToShuffle:
                            boxToRemove = ((edgeToShuffle[0], edgeToShuffle[1]), (edgeToShuffle[0], edgeToShuffle[1] + 1))  # (edgeToShuffle, (edgeToShuffle[0], edgeToShuffle[1] + 1))
                            boxes.remove(boxToRemove)
                            boxToAdd = ((edgeToShuffle[0], edgeToShuffle[1] + direction[movement][1]), (edgeToShuffle[0], edgeToShuffle[1] + direction[movement][1] + 1))  # ((edgeToShuffle[0], edgeToShuffle[1] - 1), edgeToShuffle)
                            boxes.add(boxToAdd)
                        currentPosition = (currentPosition[0], currentPosition[1] + direction[movement][1])
print("Part 2 answer:", scoreMapPart2(boxes))

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
