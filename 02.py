#!/usr/bin/python3
import numpy as np

DAY = '02'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def checkReport(report):
    rep = [int(x) for x in report.split()]
    diffs = np.diff(rep)
    return (all(x < 0 for x in diffs) or all(x > 0 for x in diffs)) and (max(abs(diffs)) < 4 and min(abs(diffs)) > 0)


def checkTolerantReport(report):
    rep = [int(x) for x in report.split()]
    for el in range(len(rep)):
        r = rep[:]
        del r[el]
        isSafe = checkReport(" ".join(map(str, r)))
        if isSafe:
            return isSafe
    return False


# part 1
correctReports = 0
for report in lines:
    correctReports += checkReport(report)
print("Part 1 answer:", correctReports)

# part 2
correctReports = 0
for report in lines:
    isSafe = checkReport(report)
    if not isSafe:
        isSafe = checkTolerantReport(report)
    correctReports += isSafe
print("Part 2 answer:", correctReports)
