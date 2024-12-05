#!/usr/bin/python3

DAY = '05'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def correctOrder(updates):
    updateOrderCorrect = True
    for updateIndex in range(len(updates)):
        if updates[updateIndex] in followingPages:
            for followingPageIndex in range(updateIndex + 1, len(updates)):
                if updates[followingPageIndex] not in followingPages[updates[updateIndex]]:
                    updateOrderCorrect = False

        if updates[updateIndex] in precedingPages:
            for precedingPageIndex in range(updateIndex - 1, -1, -1):
                if updates[precedingPageIndex] not in precedingPages[updates[updateIndex]]:
                    updateOrderCorrect = False
    return updateOrderCorrect


dealingWithRules = True
precedingPages = dict()
followingPages = dict()
runningSumOfCorrectUpdates = 0
runningSumOfIncorrectUpdates = 0
for line in lines:
    if line == '':
        dealingWithRules = False
        continue
    if dealingWithRules:
        rule = line.split('|')
        if rule[0] in followingPages:
            followingPages[rule[0]].append(rule[1])
        else:
            followingPages.update({rule[0]: [rule[1]]})
        if rule[1] in precedingPages:
            precedingPages[rule[1]].append(rule[0])
        else:
            precedingPages.update({rule[1]: [rule[0]]})

    else:
        updates = line.split(',')
        if correctOrder(updates):
            runningSumOfCorrectUpdates += int(updates[len(updates) // 2])
        else:
            while not correctOrder(updates):
                for updateIndex in range(len(updates)):
                    for followingPageIndex in range(updateIndex + 1, len(updates)):
                        if updates[followingPageIndex] in followingPages and updates[updateIndex] in followingPages[updates[followingPageIndex]]:
                            updates[updateIndex], updates[followingPageIndex] = updates[followingPageIndex], updates[updateIndex]
            runningSumOfIncorrectUpdates += int(updates[len(updates) // 2])

# part 1
print("Part 1 answer:", runningSumOfCorrectUpdates)

# part 2
print("Part 2 answer:", runningSumOfIncorrectUpdates)
