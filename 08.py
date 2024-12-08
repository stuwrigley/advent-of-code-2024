#!/usr/bin/python3

DAY = '08'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def printMap(antennas, antinodes):
    for row in range(numRows):
        str = '.' * numCols
        for col in range(numCols):
            if (row, col) in antinodes:
                str = str[:col] + '#' + str[col + 1:]
            for antenna in antennas:
                if (row, col) in antennas[antenna]:
                    str = str[:col] + antenna + str[col + 1:]
        print(str)


# part 1 and 2
numRows = len(lines)
numCols = len(lines[0])

antinodeLocationsPart1 = set()
antinodeLocationsPart2 = set()
antennaLocations = dict()

for row in range(numRows):
    for col in range(numCols):
        if lines[row][col] == '.':
            continue
        else:
            antennaFreq = lines[row][col]
            if antennaFreq not in antennaLocations:
                antennaLocations.update({antennaFreq: set()})
            antennaLocations[antennaFreq].add((row, col))

for antennaFreq in antennaLocations:
    for loc in antennaLocations[antennaFreq]:
        for otherLoc in antennaLocations[antennaFreq].difference({loc}):
            antinodeLocationsPart2.add(loc)

            distanceRows = otherLoc[0] - loc[0]
            distanceCols = otherLoc[1] - loc[1]
            antinodeRow = otherLoc[0] + distanceRows
            antinodeCol = otherLoc[1] + distanceCols

            if antinodeRow >= 0 and antinodeRow < numRows and antinodeCol >= 0 and antinodeCol < numCols:
                antinodeLocationsPart1.add((antinodeRow, antinodeCol))
                antinodeLocationsPart2.add((antinodeRow, antinodeCol))

            while True:
                antinodeRow += distanceRows
                antinodeCol += distanceCols

                if antinodeRow >= 0 and antinodeRow < numRows and antinodeCol >= 0 and antinodeCol < numCols:
                    antinodeLocationsPart2.add((antinodeRow, antinodeCol))
                else:
                    break

printMap(antennaLocations, antinodeLocationsPart1)
print("\n")
printMap(antennaLocations, antinodeLocationsPart2)

print("Part 1 answer:", len(antinodeLocationsPart1))
print("Part 2 answer:", len(antinodeLocationsPart2))
