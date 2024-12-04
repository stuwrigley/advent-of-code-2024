#!/usr/bin/python3

DAY = '04'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

WORD = "XMAS"

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def search(x, y):
    hits = 0
    if lines[y][x:x + len(WORD)] == WORD:  # forwards
        hits += 1
    if lines[y][x - (len(WORD) - 1):x + 1][::-1] == WORD:  # backwards
        hits += 1
    if y >= len(WORD) - 1:
        if lines[y][x] == WORD[0] and lines[y - 1][x] == WORD[1] and lines[y - 2][x] == WORD[2] and lines[y - 3][x] == WORD[3]:  # up
            hits += 1
        if x - 3 >= 0 and lines[y][x] == WORD[0] and lines[y - 1][x - 1] == WORD[1] and lines[y - 2][x - 2] == WORD[2] and lines[y - 3][x - 3] == WORD[3]:  # up
            hits += 1
        if x + 3 < len(lines[y]) and lines[y][x] == WORD[0] and lines[y - 1][x + 1] == WORD[1] and lines[y - 2][x + 2] == WORD[2] and lines[y - 3][x + 3] == WORD[3]:  # up
            hits += 1

    if y <= len(lines) - len(WORD):
        if lines[y][x] == WORD[0] and lines[y + 1][x] == WORD[1] and lines[y + 2][x] == WORD[2] and lines[y + 3][x] == WORD[3]:  # down
            hits += 1
        if x - 3 >= 0 and lines[y][x] == WORD[0] and lines[y + 1][x - 1] == WORD[1] and lines[y + 2][x - 2] == WORD[2] and lines[y + 3][x - 3] == WORD[3]:  # up
            hits += 1
        if x + 3 < len(lines[y]) and lines[y][x] == WORD[0] and lines[y + 1][x + 1] == WORD[1] and lines[y + 2][x + 2] == WORD[2] and lines[y + 3][x + 3] == WORD[3]:  # up
            hits += 1

    return hits


def searchMAS(x, y):
    hits = 0
    if len(lines) - 1 > y > 0 and 0 < x < len(lines[0]) - 1:
        if ((lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S") or (lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M")) and ((lines[y + 1][x - 1] == "M" and lines[y - 1][x + 1] == "S") or (lines[y + 1][x - 1] == "S" and lines[y - 1][x + 1] == "M")):
            hits += 1
    return hits


# part 1
numHits = 0
for yPos in range(len(lines)):
    for xPos in range(len(lines[0])):
        if lines[yPos][xPos] == WORD[0]:
            numHits += search(xPos, yPos)
print("Part 1 answer:", numHits)

# part 2
numHits = 0
for yPos in range(len(lines)):
    for xPos in range(len(lines[0])):
        if lines[yPos][xPos] == "A":
            numHits += searchMAS(xPos, yPos)
print("Part 2 answer:", numHits)
