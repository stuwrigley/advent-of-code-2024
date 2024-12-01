#!/usr/bin/python3
import numpy as np
from collections import Counter

DAY = '01'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

lists = np.array([[int(y) for y in x.split()] for x in lines])
sortedLists = np.sort(np.transpose(lists))

# part 1
print("Part 1 answer:", sum(np.absolute(np.diff(sortedLists, axis=0)[0])))

# part 2
list1Counts = Counter(sortedLists[0, :])
list2Counts = Counter(sortedLists[1, :])
similarityScore = 0
for num in list1Counts:
    similarityScore += num * list1Counts[num] * list2Counts[num]
print("Part 2 answer:", similarityScore)
