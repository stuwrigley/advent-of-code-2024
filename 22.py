#!/usr/bin/python3
import time

start_time = time.time()

DAY = '22'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [int(line.rstrip()) for line in f]


def evolve(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ int(num / 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num


# part 1
total = 0
for secret in lines:
    for step in range(2000):
        secret = evolve(secret)
    total += secret
print("Part 1 answer:", total)

# part 2
print("Part 2 answer:")

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
