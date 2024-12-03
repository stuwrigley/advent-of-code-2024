#!/usr/bin/python3
import re

DAY = '03'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def processInstruction(mul):
    parts = mul.split(',')
    return int(parts[0][4:]) * int(parts[1][:-1])


# part 1
regex = r'mul\(\d{1,3},\d{1,3}\)'
runningSum = 0
for line in lines:
    matches = re.finditer(regex, line)
    for match in matches:
        runningSum += processInstruction(match.group())
print("Part 1 answer:", runningSum)

# part 2
regex = r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)'
addToRunningSum = True
runningSum = 0
for line in lines:
    matches = re.finditer(regex, line)
    for match in matches:
        if match.group() == "do()":
            addToRunningSum = True
            continue
        if match.group() == "don't()":
            addToRunningSum = False
            continue
        if addToRunningSum:
            runningSum += processInstruction(match.group())
print("Part 2 answer:", runningSum)
