#UVA - 10071
from sys import stdin

def main():

    lines = stdin.readlines()

    for line in lines:
        if line.strip():
            v, t = map(int, line.split())
            distance = v * t * 2
            print(distance)

if __name__ == '__main__':
    main()