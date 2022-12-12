from collections import deque
import copy
import fileinput
from heapq import heapify, heappop

def main():
    filename = '11.txt'
    #filename = '11-example.txt'

    monkeys = []
    f = fileinput.input(files=filename)
    line = f.readline()
    while line:
        # skip monkey line
        line = f.readline()

        items = deque(line.strip()[16:].split(', '))
        operation = f.readline().strip()[17:].split(' ')
        test = f.readline().strip()[19:]
        trueMonkey = f.readline().strip()[25:]
        falseMonkey = f.readline().strip()[26:]

        monkey = {
            'items': items,
            'operation': operation,
            'test': test,
            'ifTrue': trueMonkey,
            'ifFalse': falseMonkey,
        }
        monkeys.append(monkey)

        # skip separating newline
        f.readline()
        line = f.readline()

    print(part1(monkeys))
    print(part2(monkeys))

def part1(monkeys):
    monkeys = copy.deepcopy(monkeys)
    monkeyBusiness = 0

    inspects = [0 for _ in range(len(monkeys))]
    for round in range(20):
        for i,monkey in enumerate(monkeys):
            while len(monkey['items']):
                item = monkey['items'].popleft()
                worry = int(item)

                # apply operator
                applyValue = worry if monkey['operation'][2] == 'old' else int(monkey['operation'][2])
                if monkey['operation'][1] == '+':
                    worry += applyValue
                else:
                    worry *= applyValue

                # apply relief modifier
                worry //= 3

                # increment inspection for monkey
                inspects[i] += 1

                # get test result
                testResult = worry % int(monkey['test']) == 0

                # send item to resulting monkey
                nextMonkey = int(monkey['ifTrue']) if testResult else int(monkey['ifFalse'])
                #print(item,monkey['operation'],worry,monkey['test'],nextMonkey)
                monkeys[nextMonkey]['items'].append(worry)

    #print(inspects)
    monkeyActivity = [(-count, monkey) for monkey,count in enumerate(inspects)]
    heapify(monkeyActivity)

    monkeyBusiness = -heappop(monkeyActivity)[0]
    monkeyBusiness *= -heappop(monkeyActivity)[0]

    return monkeyBusiness

def part2(monkeys):
    monkeys = copy.deepcopy(monkeys)
    monkeyBusiness = 0

    # get large divisor to adjust worry levels
    divisor = 1
    for monkey in monkeys:
        divisor *= int(monkey['test'])

    inspects = [0 for _ in range(len(monkeys))]
    for round in range(10000):
        for i,monkey in enumerate(monkeys):
            while len(monkey['items']):
                item = monkey['items'].popleft()
                worry = int(item)

                # apply operator
                applyValue = worry if monkey['operation'][2] == 'old' else int(monkey['operation'][2])
                if monkey['operation'][1] == '+':
                    worry += applyValue
                else:
                    worry *= applyValue

                worry %= divisor

                # increment inspection for monkey
                inspects[i] += 1

                # get test result
                testResult = worry % int(monkey['test']) == 0

                # send item to resulting monkey
                nextMonkey = int(monkey['ifTrue']) if testResult else int(monkey['ifFalse'])
                #print(item,monkey['operation'],worry,monkey['test'],nextMonkey)
                monkeys[nextMonkey]['items'].append(worry)

        if round == 0 or round == 19 or round == 999:
            print(inspects)

    #print(inspects)
    monkeyActivity = [(-count, monkey) for monkey,count in enumerate(inspects)]
    heapify(monkeyActivity)

    monkeyBusiness = -heappop(monkeyActivity)[0]
    monkeyBusiness *= -heappop(monkeyActivity)[0]

    return monkeyBusiness

if __name__ == '__main__':
    main()
