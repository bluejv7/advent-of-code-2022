import fileinput

def main():
    pairs = []
    for line in fileinput.input(files=('4.txt')):
        line = line.strip()
        if line == '':
            break
        pairs.append(line.split(','))

    #pairs = [
    #    ('2-4','6-8'),
    #    ('2-3','4-5'),
    #    ('5-7','7-9'),
    #    ('2-8','3-7'),
    #    ('6-6','4-6'),
    #    ('2-6','4-8'),
    #]
    print(part1(pairs))
    print(part2(pairs))

def part1(pairs):
    total = 0
    for pair in pairs:
        first = tuple(map(int, pair[0].split('-')))
        second = tuple(map(int, pair[1].split('-')))
        if first[0] > second[0]:
            first, second = second, first

        if first[0] <= second[0] and first[1] >= second[1]:
            total += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            total += 1

    return total

def part2(pairs):
    total = 0
    for pair in pairs:
        first = tuple(map(int, pair[0].split('-')))
        second = tuple(map(int, pair[1].split('-')))
        if first[0] > second[0]:
            first, second = second, first

        if first[0] > second[1] or first[1] < second[0]:
            continue
        if second[0] > first[1] or second[1] < first[0]:
            continue

        total += 1

    return total

if __name__ == '__main__':
    main()
