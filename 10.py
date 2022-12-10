from collections import deque
import fileinput

def main():
    filename = '10.txt'
    #filename = '10-example.txt'

    commands = []
    for line in fileinput.input(files=filename):
        line = line.strip()
        (op,arg) = (line,None) if line == 'noop' else line.split(' ')
        if arg != None:
            arg = int(arg)
        commands.append((op, arg))

    print(part1(commands))
    print(part2(commands))

def part1(commands):
    totalSignalStrength = 0

    x = 1
    cycle = 0
    addxQueue = deque()
    for command in commands:
        cycle += 1
        if len(addxQueue):
            val = addxQueue.popleft()
            x += val
        if cycle % 40 == 20:
            totalSignalStrength += cycle * x
        if command[0] == 'addx':
            addxQueue.append(command[1])
            cycle += 1
            if cycle % 40 == 20:
                totalSignalStrength += cycle * x

    return totalSignalStrength

def part2(commands):
    output = ''

    x = 1
    i = 0
    cycle = 0
    processing = []
    while cycle <= 240:
        cycle += 1
        if len(processing) and processing[0][0] == cycle:
            x += processing[0][1]
            processing.pop()
        if not len(processing):
            if i < len(commands) and commands[i][0] == 'addx':
                processing.append((cycle+2, commands[i][1]))
            i += 1

        hpos = (cycle-1) % 40
        char = '#' if hpos >= x-1 and hpos <= x+1 else '.'
        output = ''.join((output, char))

        if cycle % 40 == 0:
            output = ''.join((output, "\n"))

    return output

if __name__ == '__main__':
    main()
