#!/usr/bin/python3
import time

start_time = time.time()

DAY = '25'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

locks = []
keys = []

for lineID in range(0, len(lines), 8):
    thisSchematic = None
    if lines[lineID] == "#####":  # lock
        thisSchematic = locks
        searchChar = "#"
    else:  # key
        thisSchematic = keys
        searchChar = "."
    item = []
    for col in range(5):
        count = 0
        for row in range(5):
            count += lines[lineID + row + 1][col] == "#"
        item.append(count)
    thisSchematic.append(item)

# part 1
pairs = 0
for key in keys:
    for lock in locks:
        noOverlap = True
        for col in range(5):
            if key[col] + lock[col] > 5:
                noOverlap = False
                break
        pairs += noOverlap

print("Part 1 answer:", pairs)

# part 2
print("Part 2 answer:")

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
