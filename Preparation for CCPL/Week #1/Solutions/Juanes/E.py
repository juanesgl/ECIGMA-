#R2 Kattis

from sys import stdin

def main():


    lines = stdin.readlines()

    for line in lines:

        if line.strip():
            R1,S = map(int, line.split())
            R2 = 2 * S - R1
            print(R2)

if __name__ == '__main__':
    main()