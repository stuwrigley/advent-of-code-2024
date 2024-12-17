#!/usr/bin/python3
import math
import time

start_time = time.time()

DAY = '17'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

A = int(lines[0].split(":")[1])
B = int(lines[1].split(":")[1])
C = int(lines[2].split(":")[1])
program = [int(x) for x in lines[4].split(":")[1].split(",")]


def getComboOperand(operand, A, B, C):
    comboOperand = operand
    if operand == 4:
        comboOperand = A
    if operand == 5:
        comboOperand = B
    if operand == 6:
        comboOperand = C
    if operand == 7:
        print("Reserved operand!")
    return comboOperand


def runProgram(A, B, C, program, part2):
    output = ""
    instructionPointer = 0
    while instructionPointer < len(program) - 1:
        opcode = program[instructionPointer]
        operand = program[instructionPointer + 1]

        if opcode == 0:  # adv
            A = int(A / (math.pow(2, getComboOperand(operand, A, B, C))))
        elif opcode == 1:  # bxl
            B = B ^ operand
        elif opcode == 2:  # bst
            B = getComboOperand(operand, A, B, C) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                instructionPointer = operand
                continue
        elif opcode == 4:  # bxc
            B = B ^ C
        elif opcode == 5:  # out
            if len(output) != 0:
                output += ","
            output += str(getComboOperand(operand, A, B, C) % 8)
        elif opcode == 6:  # bdv
            B = int(A / (math.pow(2, getComboOperand(operand, A, B, C))))
        elif opcode == 7:  # cdv
            C = int(A / (math.pow(2, getComboOperand(operand, A, B, C))))

        instructionPointer += 2
    return output


# part 1
print("Part 1 answer:", runProgram(A, B, C, program, False))

# part 2

if TEST:
    A = 2024
    B = 0
    C = 0
    program = [0, 3, 5, 4, 3, 0]

for possibleA in range(20000000000):
    if possibleA == A:
        continue
    output = runProgram(possibleA, B, C, program, True)
    if [int(x) for x in output.split(",")] == program:
        print("Part 2 answer:", possibleA)
        break

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
