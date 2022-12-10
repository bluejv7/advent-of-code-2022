import fileinput

def main():
    moves = []
    for line in fileinput.input(files=('2.txt')):
        line = line.strip()
        if line == '':
            break

        (opponent, player) = line.split(' ')
        moves.append((opponent, player))
    #moves = [
    #    ('A', 'Y'),
    #    ('B', 'X'),
    #    ('C', 'Z'),
    #]

    print(part1(moves))
    print(part2(moves))

def part1(moves):
    score = 0

    for move in moves:
        # 0-1-2: rock-paper-scissors
        playerMove = ord(move[1]) - ord('X')
        opponentMove = ord(move[0]) - ord('A')

        score += playerMove + 1
        if playerMove == opponentMove:
            score += 3
        elif playerMove == (opponentMove + 1) % 3:
            score += 6

    return score

def part2(moves):
    score = 0

    for move in moves:
        opponentMove = ord(move[0]) - ord('A')
        if move[1] == 'X':
            playerMove = (opponentMove - 1) % 3
        elif move[1] == 'Y':
            playerMove = opponentMove
            score += 3
        else:
            playerMove = (opponentMove + 1) % 3
            score += 6

        score += playerMove + 1

    return score

if __name__ == '__main__':
    main()
