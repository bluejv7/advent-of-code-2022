from collections.abc import Sequence
import fileinput
from functools import cmp_to_key
import json

def main():
    filename = '13.txt'
    #filename = '13-example.txt'

    pairs = []
    f = fileinput.input(files=filename)
    line = f.readline()
    while line:
        pairs.append((json.loads(line.strip()), json.loads(f.readline().strip())))
        f.readline()
        line = f.readline()

    print(part1(pairs))
    print(part2(pairs))

def part1(pairs):
    score = 0

    for i,pair in enumerate(pairs):
        if isRight(pair[0], pair[1]) == -1:
            score += i+1

    return score

def part2(pairs):
    decoderKey = 1

    packets = [[[2]], [[6]]]
    for pair in pairs:
        packets.append(pair[0])
        packets.append(pair[1])
    packets.sort(key=cmp_to_key(isRight))

    for i,packet in enumerate(packets):
        if packet == [[2]]:
            decoderKey *= i+1
        elif packet == [[6]]:
            decoderKey *= i+1
            break

    return decoderKey

def isRight(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if left > right:
            return 1
        return 0

    left = [left] if not isinstance(left, Sequence) else left
    right = [right] if not isinstance(right, Sequence) else right

    for i in range(min(len(left), len(right))):
        elementRightValue = isRight(left[i], right[i])
        if elementRightValue == 0:
            continue
        return elementRightValue

    if len(left) < len(right):
        return -1
    if len(left) == len(right):
        return 0
    return 1

if __name__ == '__main__':
    main()
