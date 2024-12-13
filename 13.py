#!/usr/bin/python3
import time

start_time = time.time()

DAY = '13'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

machines = []
for lineID in range(0, len(lines), 4):
    aX = int(lines[lineID].split()[2].split("+")[1].split(",")[0])
    aY = int(lines[lineID].split()[3].split("+")[1])
    bX = int(lines[lineID + 1].split()[2].split("+")[1].split(",")[0])
    bY = int(lines[lineID + 1].split()[3].split("+")[1])
    prizeX = int(lines[lineID + 2].split()[1].split("=")[1].split(",")[0])
    prizeY = int(lines[lineID + 2].split()[2].split("=")[1].split(",")[0])
    machines.append([[aX, aY], [bX, bY], [prizeX, prizeY]])


def processMachine(machine):
    numTokens = 0
    factor = machine[0][0] / (-1 * machine[0][1])
    numPushesB = (machine[2][1] * factor + machine[2][0]) / (machine[1][1] * factor + machine[1][0])
    numPushesA = (machine[2][0] - (numPushesB * machine[1][0])) / machine[0][0]
    if abs(round(numPushesA) - numPushesA) < 0.01 and abs(round(numPushesB) - numPushesB) < 0.01:
        numTokens += (round(numPushesA) * 3) + round(numPushesB)
    return numTokens


# part 1
numTokens = 0
for machine in machines:
    numTokens += processMachine(machine)
print("Part 1 answer:", numTokens)

# part 2
numTokens = 0
for machine in machines:
    machine[2][0] += 10000000000000
    machine[2][1] += 10000000000000
    numTokens += processMachine(machine)
print("Part 2 answer:", numTokens)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
