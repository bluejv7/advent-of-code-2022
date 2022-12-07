from bisect import bisect_left, insort
from collections import deque
import fileinput

def main():
    file = '7.txt'
    #file = '7-example.txt'

    root = Node('/', None)
    cur = root
    lastCommand = None
    for line in fileinput.input(files=(file)):
        line = line.strip()

        isCommand = line[0] == '$'
        if isCommand:
            lastCommand = line[2:4]
            if lastCommand == 'cd':
                cdArg = line[5:]
                if cdArg == '/':
                    cur = root
                elif cdArg == '..':
                    cur = cur.parent
                else:
                    cur = cur.nodes[cdArg]
        else:
            # assume last command is ls
            if line[0] == 'd':
                folder = line[4:]
                cur.nodes[folder] = Node(folder, cur)
            else:
                (size, name) = line.split(' ')
                cur.files[name] = int(size)

                _cur = cur
                while _cur:
                    _cur.size += int(size)
                    _cur = _cur.parent

    #root.print()
    print(part1(root))
    print(part2(root))

def part1(root):
    total = 0

    stack = [root]
    while len(stack):
        node = stack.pop()
        if node.size <= 100000:
            total += node.size

        for n in node.nodes.values():
            stack.append(n)

    return total

def part2(root):
    totalSpace = 70000000
    unused = totalSpace - root.size
    target = 30000000 - unused

    sizes = []
    stack = [root]
    while len(stack):
        node = stack.pop()
        insort(sizes, node.size)

        for n in node.nodes.values():
            stack.append(n)

    closestIndex = bisect_left(sizes, target)
    return sizes[closestIndex] if sizes[closestIndex] >= target else sizes[closestIndex-1]

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.nodes = {}
        self.files = {}
        self.size = 0

    def print(self):
        stack = [(0, self)]
        seen = set()
        while(len(stack)):
            (level, node) = stack.pop()
            seen.add(node)
            print('  ' * level + node.name)

            for n in node.nodes.values():
                if n not in seen:
                    stack.append((level + 1, n))

            for name, size in node.files.items():
                print('  '*(level+1) + name, size)

if __name__ == '__main__':
    main()
