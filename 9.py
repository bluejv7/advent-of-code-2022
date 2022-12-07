import fileinput

def main():
    filename = '9.txt'
    #filename = '9-example.txt'
    #filename = '9-example2.txt'

    commands = []
    for line in fileinput.input(files=(filename)):
        line = line.strip()
        (direction, steps) = line.split(' ')
        commands.append((direction, int(steps)))

    print(part1(commands))
    print(part2(commands))

def part1(commands):
    seen = set()
    head = [0,0]
    tail = [0,0]
    for command in commands:
        incr = 0
        coord = 0
        if command[0] == 'U':
            incr = 1
            coord = 0
        elif command[0] == 'D':
            incr = -1
            coord = 0
        elif command[0] == 'L':
            incr = -1
            coord = 1
        else:
            incr = 1
            coord = 1

        for i in range(command[1]):
            head[coord] += incr
            if tail[coord] == head[coord] - 2*incr:
                tail[coord] += incr
                tail[1-coord] = head[1-coord]
            if (tail[0], tail[1]) not in seen:
                seen.add((tail[0], tail[1]))

    return len(seen)

def part2(commands):
    seen = set()
    rope = [[0,0] for _ in range(10)]
    for command in commands:
        incr = 0
        coord = 0
        if command[0] == 'U':
            incr = 1
            coord = 0
        elif command[0] == 'D':
            incr = -1
            coord = 0
        elif command[0] == 'L':
            incr = -1
            coord = 1
        else:
            incr = 1
            coord = 1

        for i in range(command[1]):
            rope[0][coord] += incr
            for j in range(1,len(rope)):
                x = rope[j-1][0] - rope[j][0]
                y = rope[j-1][1] - rope[j][1]
                if abs(x) == 2 and abs(y) == 2:
                    rope[j][0] += x // 2
                    rope[j][1] += y // 2
                elif abs(x) == 2:
                    rope[j][0] += x // 2
                    rope[j][1] = rope[j-1][1]
                elif abs(y) == 2:
                    rope[j][0] = rope[j-1][0]
                    rope[j][1] += y // 2

            print(rope[9])
            if (rope[9][0],rope[9][1]) not in seen:
                seen.add((rope[9][0], rope[9][1]))

    return len(seen)

if __name__ == '__main__':
    main()

"""
... ... ..H
... ..H .21
21H 21. ...
00 10 20
00 10 21
11 21 22
"""
