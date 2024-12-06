#!/usr/bin/python3

DAY = '06'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

NEXTPOS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
curDirectionIndex = 0

# find guard position (assuming guard starts looking "up")
guardPosition = [0, 0]
for counter, line in enumerate(lines):
    guardPosition[1] = counter
    guardPosition[0] = line.find('^')
    if guardPosition[0] > -1:
        break
startingPosition = (guardPosition[0], guardPosition[1])


def posCanMakeLoop(startPos, dir):
    curPos = startPos
    visited = set()
    visited.add(tuple(curPos + NEXTPOS[dir]))
    newBlocker = [startPos[0] + NEXTPOS[dir][0], startPos[1] + NEXTPOS[dir][1]]  # let's try blocking in front of the guard and see of a loop happens
    curDirectionIndex = (dir + 1) % len(NEXTPOS)  # new blocker forces us to turn right
    visited.add(tuple(curPos + NEXTPOS[curDirectionIndex]))
    while True:
        nextPos = [curPos[0] + NEXTPOS[curDirectionIndex][0], curPos[1] + NEXTPOS[curDirectionIndex][1]]
        if nextPos[0] < 0 or nextPos[0] >= len(lines[0]) or nextPos[1] < 0 or nextPos[1] >= len(lines):  # move takes us off the map
            return False
        if lines[nextPos[1]][nextPos[0]] != '#' and nextPos != newBlocker:  # if the next step isn't an existing blocker or the new one...
            curPos = nextPos
            if tuple(curPos + NEXTPOS[curDirectionIndex]) in visited:  # we've already been at this position travelling in the same direction. We must have looped.
                return True
            else:
                visited.add(tuple(curPos + NEXTPOS[curDirectionIndex]))
        else:  # we're facing an existing blocker or the new one so turn right
            curDirectionIndex = (curDirectionIndex + 1) % len(NEXTPOS)


# part 1 and 2
visited = set()
visited.add(tuple(guardPosition))
obstructionPosition = set()
while True:
    nextPos = [guardPosition[0] + NEXTPOS[curDirectionIndex][0], guardPosition[1] + NEXTPOS[curDirectionIndex][1]]
    if nextPos[0] < 0 or nextPos[0] >= len(lines[0]) or nextPos[1] < 0 or nextPos[1] >= len(lines):  # move takes us off the map
        break
    if lines[nextPos[1]][nextPos[0]] != '#':  # if the next step isn't a blocker...
        if tuple(nextPos) not in visited:  # if we haven't been here before...
            visited.add(tuple(nextPos))
            if posCanMakeLoop(guardPosition, curDirectionIndex):  # part 2 - see if adding a new obstacle at this point makes a loop
                obstructionPosition.add(tuple(nextPos))
        guardPosition = nextPos
    else:  # we're facing an existing blocker or the new one so turn right
        curDirectionIndex = (curDirectionIndex + 1) % len(NEXTPOS)

print("Part 1 answer:", len(visited))
print("Part 2 answer:", len(obstructionPosition))
