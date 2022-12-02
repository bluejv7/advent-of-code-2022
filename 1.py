import fileinput
from heapq import heappush, heappop

def main():
    elfSnacks = []
    cur = []
    for line in fileinput.input(files = '1.txt'):
        if line == "\n":
            elfSnacks.append(cur)
            cur = []
        else:
            cur.append(line.replace("\n", ""))

    print(part1(elfSnacks))
    print(part2(elfSnacks))

def part1(elfSnacks):
    mostCalories = 0
    for elfInventory in elfSnacks:
        curCalories = 0
        for calorie in elfInventory:
            curCalories += int(calorie)
        if mostCalories < curCalories:
            mostCalories = curCalories

    return mostCalories


def part2(elfSnacks):
    mostCalories = []
    for elfInventory in elfSnacks:
        curCalories = 0
        for calorie in elfInventory:
            curCalories += int(calorie)
        heappush(mostCalories, curCalories)

        if len(mostCalories) > 3:
            heappop(mostCalories)

    totalCalories = 0
    for calories in mostCalories:
        totalCalories += calories

    return totalCalories


if __name__ == '__main__':
    main()
