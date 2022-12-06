import fileinput

def main():
    datastream = ''
    for line in fileinput.input(files=('6.txt')):
        line = line.strip()
        datastream += line

    #datastream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    #datastream = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    print(part1(datastream))

def part1(datastream):
    chars = {datastream[0]}
    left = 0
    right = 1
    while len(chars) < 4:
        while datastream[right] in chars:
            chars.remove(datastream[left])
            left += 1
        chars.add(datastream[right])
        right += 1

    return right

def part1(datastream):
    chars = {datastream[0]}
    left = 0
    right = 1
    while len(chars) < 14:
        while datastream[right] in chars:
            chars.remove(datastream[left])
            left += 1
        chars.add(datastream[right])
        right += 1

    return right

if __name__ == '__main__':
    main()
