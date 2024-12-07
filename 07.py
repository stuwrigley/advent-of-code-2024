#!/usr/bin/python3

DAY = '07'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def validCalibration(target, numbers, doPart2):
    if len(numbers) == 1:
        return target == numbers[0]
    if validCalibration(target, [numbers[0] + numbers[1]] + numbers[2:], doPart2):
        return True
    if validCalibration(target, [numbers[0] * numbers[1]] + numbers[2:], doPart2):
        return True
    if doPart2 and validCalibration(target, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], doPart2):
        return True
    return False


# part 1 and 2
testValueSumPart1 = 0
testValueSumPart2 = 0
for line in lines:
    parts = line.split(':')
    target = int(parts[0])
    numbers = [int(x) for x in parts[1].split()]
    if validCalibration(target, numbers, False):
        testValueSumPart1 += target
    if validCalibration(target, numbers, True):
        testValueSumPart2 += target
print("Part 1 answer:", testValueSumPart1)
print("Part 2 answer:", testValueSumPart2)
