import copy
from collections import deque
import fileinput

def main():
    stacks = []
    commands = []
    for line in fileinput.input(files=('5.txt')):
        line = line.strip()

        if line == '':
            continue
        if line[0] == '[':
            for i in range(0, len(line), 4):
                if len(stacks) <= i // 4:
                    stacks.append(deque())
                if line[i] != '[':
                    continue
                stacks[i//4].appendleft(line[i+1])
        elif line[0] == 'm':
            amount = int(line[5:line.find(' from')])
            fromIndex = int(line[line.find(' from')+6:line.find(' to')])
            toIndex = int(line[line.find(' to')+4:])
            commands.append((amount, fromIndex, toIndex))

    #stacks = [
    #    ['Z', 'N'],
    #    ['M', 'C', 'D'],
    #    ['P'],
    #]
    #commands = [
    #    (1, 2, 1),
    #    (3, 1, 3),
    #    (2, 2, 1),
    #    (1, 1, 2),
    #]
    print(part1(stacks, commands))
    print(part2(stacks, commands))

def part1(stacks, commands):
    stacks = copy.deepcopy(stacks)
    commands = copy.deepcopy(commands)

    for command in commands:
        for _ in range(0, command[0]):
            stacks[command[2]-1].append(stacks[command[1]-1].pop())

    message = ''
    for stack in stacks:
        message += stack[-1]

    return message

def part2(stacks, commands):
    stacks = copy.deepcopy(stacks)
    commands = copy.deepcopy(commands)

    for command in commands:
        queue = deque()
        print(stacks)
        print(command)
        for _ in range(0, command[0]):
            queue.appendleft(stacks[command[1]-1].pop())
        while(len(queue)):
            stacks[command[2]-1].append(queue.popleft())

    message = ''
    for stack in stacks:
        message += stack[-1]

    return message

if __name__ == '__main__':
    main()
