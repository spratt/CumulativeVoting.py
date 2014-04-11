import sys
import random

def main():
    path = sys.argv[1]
    lines = []
    with open(path, 'r') as f:
        for line in f:
            lines.append(line)
    random.shuffle(lines)
    for line in lines:
        print(line, end="")

if __name__ == '__main__':
    main()
