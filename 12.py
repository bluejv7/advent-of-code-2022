from collections import deque
import fileinput

def main():
    filename = '12.txt'
    #filename = '12-example.txt'

    map = []
    S = None
    for i,line in enumerate(fileinput.input(files=filename)):
        line = line.strip()
        map.append(line)
        SIndex = line.find('S')
        if SIndex != -1:
            S = (i, SIndex)

    print(part1(map, S))
    print(part2(map, S))

def part1(map, S):
    M = len(map)
    N = len(map[0])

    queue = deque([(S,'a',0)])
    seen = {S}
    while len(queue):
        pos, elevation, steps = queue.popleft()
        if elevation == 'E':
            return steps

        row,col = pos

        newPos = (row-1,col)
        if pos[0] > 0 and newPos not in seen and canClimb(elevation, map[newPos[0]][newPos[1]]):
            seen.add(newPos)
            queue.append((newPos, map[newPos[0]][newPos[1]], steps+1))

        newPos = (row+1,col)
        if pos[0] < M-1 and newPos not in seen and canClimb(elevation, map[newPos[0]][newPos[1]]):
            seen.add(newPos)
            queue.append((newPos, map[newPos[0]][newPos[1]], steps+1))

        newPos = (row,col-1)
        if pos[1] > 0 and newPos not in seen and canClimb(elevation, map[newPos[0]][newPos[1]]):
            seen.add(newPos)
            queue.append((newPos, map[newPos[0]][newPos[1]], steps+1))

        newPos = (row,col+1)
        if pos[1] < N-1 and newPos not in seen and canClimb(elevation, map[newPos[0]][newPos[1]]):
            seen.add(newPos)
            queue.append((newPos, map[newPos[0]][newPos[1]], steps+1))

    return -1

def part2(map, S):
    M = len(map)
    N = len(map[0])

    queue = deque([(S,'a',0)])
    seen = {S}

    for i,line in enumerate(map):
        for j,elevation in enumerate(line):
            if elevation == 'a':
                queue.append(((i,j), elevation, 0))
                seen.add((i,j))

    while len(queue):
        pos, elevation, steps = queue.popleft()
        if elevation == 'E':
            return steps

        row,col = pos

        newPos = (row-1,col)
        if pos[0] > 0 and newPos not in seen and canClimb(elevation, map[newPos[0]][newPos[1]]):
            seen.add(newPos)
            queue.append((newPos, map[newPos[0]][newPos[1]], steps+1))

        newPos = (row+1,col)
        if pos[0] < M-1 and newPos not in seen and canClimb(elevation, map[newPos[0]][newPos[1]]):
            seen.add(newPos)
            queue.append((newPos, map[newPos[0]][newPos[1]], steps+1))

        newPos = (row,col-1)
        if pos[1] > 0 and newPos not in seen and canClimb(elevation, map[newPos[0]][newPos[1]]):
            seen.add(newPos)
            queue.append((newPos, map[newPos[0]][newPos[1]], steps+1))

        newPos = (row,col+1)
        if pos[1] < N-1 and newPos not in seen and canClimb(elevation, map[newPos[0]][newPos[1]]):
            seen.add(newPos)
            queue.append((newPos, map[newPos[0]][newPos[1]], steps+1))

    return -1

def canClimb(start, dest):
    if dest != 'E':
        return ord(start) + 1 >= ord(dest)
    return ord(start) >= ord('y') and dest == 'E'

if __name__ == '__main__':
    main()
