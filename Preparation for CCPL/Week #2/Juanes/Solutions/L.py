from sys import stdin 


def is_od_or_even(x):

    if x % 2 == 0:
        print(f'{x} is even')

    else:

        print(f'{x} is odd')

def main():
    TC = int(stdin.readline())


    for _ in range(TC):
        x = int(stdin.readline())
        is_od_or_even(x)

if __name__ == '__main__':
    main()