import fileinput

def main():
    rucksacks = []
    for line in fileinput.input(files=['3.txt']):
        line = line.strip()
        if line == '':
            break

        rucksacks.append(line)

    print(part1(rucksacks))
    #print(part1([
    #    'vJrwpWtwJgWrhcsFMMfFFhFp',
    #    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    #    'PmmdzqPrVvPwwTWBwg',
    #    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    #    'ttgJtRGJQctTZtZT',
    #    'CrZsJsPPZsGzwwsLwLmpwMDw',
    #]))
    print(part2(rucksacks))
    print(part2([
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw',
    ]))

def part1(rucksacks):
    totalPriority = 0

    for rucksack in rucksacks:
        items = set()
        compSize = len(rucksack) // 2
        for i in range(compSize):
            items.add(rucksack[i])

        for item in rucksack[compSize:]:
            if item in items:
                if item < 'a':
                    totalPriority += ord(item) - ord('A') + 27
                else:
                    totalPriority += ord(item) - ord('a') + 1
                break

    return totalPriority

def part2(rucksacks) -> int:
    totalPriority = 0

    for i in range(0, len(rucksacks), 3):
        rucksackSets = (set(), set())
        for j in range(i, i+2):
            for item in rucksacks[j]:
                rucksackSets[j-i].add(item)

        for item in rucksacks[i+2]:
            if item in rucksackSets[0] and item in rucksackSets[1]:
                if item < 'a':
                    totalPriority += ord(item) - ord('A') + 27
                else:
                    totalPriority += ord(item) - ord('a') + 1
                break

    return totalPriority

if __name__ == '__main__':
    main()
