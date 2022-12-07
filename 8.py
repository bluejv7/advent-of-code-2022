import fileinput

def main():
    filename = '8.txt'
    #filename = '8-example.txt'

    grid = []
    for line in fileinput.input(files=(filename)):
        line = line.strip()
        grid.append(line)

    print(part1(grid))
    print(part2(grid))

def part1(grid):
    M = len(grid)
    N = len(grid[0])

    seen = set()
    colView = [0 for _ in range(N)]
    for i in range(M):
        largestLeft = 0
        for j,col in enumerate(grid[i]):
            colVal = int(col)
            if (i,j) not in seen and (i == 0 or j == 0 or colVal > largestLeft or colVal > colView[j]):
                seen.add((i,j))
            if colVal > largestLeft:
                largestLeft = colVal
            if colVal > colView[j]:
                colView[j] = colVal

    colView = [0 for _ in range(N)]
    for i in range(M-1,-1,-1):
        largestRight = 0
        for j in range(N-1,-1,-1):
            colVal = int(grid[i][j])
            if (i,j) not in seen and (i == M-1 or j == N-1 or colVal > largestRight or colVal > colView[j]):
                seen.add((i,j))
            if colVal > largestRight:
                largestRight = colVal
            if colVal > colView[j]:
                colView[j] = colVal

    return len(seen)

def part2(grid):
    maxScore = 0
    for i,row in enumerate(grid):
        for j,col in enumerate(grid[i]):
            val = int(col)

            score = 1
            score *= scoreDirection(grid,i-1,j,'u',val)
            score *= scoreDirection(grid,i+1,j,'d',val)
            score *= scoreDirection(grid,i,j-1,'l',val)
            score *= scoreDirection(grid,i,j+1,'r',val)

            if score > maxScore:
                maxScore = score

    return maxScore

def scoreDirection(grid, i, j, direction, val):
    M = len(grid)
    N = len(grid[0])

    if i < 0 or i > M-1 or j < 0 or j > N-1:
        return 0

    curVal = int(grid[i][j])
    if direction == 'u':
        if val > curVal:
            return 1 + scoreDirection(grid,i-1,j,direction,val)
    elif direction == 'd':
        if val > curVal:
            return 1 + scoreDirection(grid,i+1,j,direction,val)
    elif direction == 'l':
        if val > curVal:
            return 1 + scoreDirection(grid,i,j-1,direction,val)
    else:
        if val > curVal:
            return 1 + scoreDirection(grid,i,j+1,direction,val)

    return 1

if __name__ == '__main__':
    main()

"""
30373
25512
65332
33549
35390

O(MN) * 4
"""
