#!/usr/bin/python3
from collections import deque

DAY = '09'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def checksum(disk):
    checksum = 0
    for count, fileID in enumerate(disk):
        if fileID is not None:
            checksum += count * fileID
    return checksum


files = deque([])
spaces = deque([])

disk = []
fileID = 0
position = 0
for count, char in enumerate(lines[0]):
    if count % 2 == 0:  # file
        files.append((position, int(char), fileID))  # this is only for part 2
        for i in range(int(char)):
            disk.append(fileID)
            position += 1
        fileID += 1
    else:  # space
        spaces.append((position, int(char)))  # this is only for part 2
        for i in range(int(char)):
            disk.append(None)
            position += 1

part2Disk = disk[:]

endPoint = len(disk) - 1
for count, block in enumerate(disk):
    if count == endPoint:
        break
    if block == None:
        while disk[endPoint] == None:
            endPoint -= 1
        disk[count] = disk[endPoint]
        disk[endPoint] = None
print("Part 1 answer:", checksum(disk))

for (filePosition, fileSize, fileID) in reversed(files):
    for spaceCount, (spacePosition, spaceSize) in enumerate(spaces):
        if spacePosition < filePosition and fileSize <= spaceSize:
            for i in range(fileSize):
                part2Disk[filePosition + i] = None
                part2Disk[spacePosition + i] = fileID
            spaces[spaceCount] = (spacePosition + fileSize, spaceSize - fileSize)
            break
print("Part 2 answer:", checksum(part2Disk))
