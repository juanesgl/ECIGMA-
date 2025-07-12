#UVA - 11805

from sys import stdin

def main():

    TC = int(stdin.readline().strip())
    case = 1

    for _ in range(TC):
        N, K , P = map(int, stdin.readline().strip().split())

        formula = ((K  - 1 + P) % N) + 1

        print(f'Case {case}: {formula}')
        case += 1

if __name__ == '__main__':
    main()