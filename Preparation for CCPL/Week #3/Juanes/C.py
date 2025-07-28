from sys import stdin 

def tines_finder(l, r):

    if l == 0 and r == 0:
        print(f'Not a moose')

    elif l == r:

        multi = 2 * l

        print(f'Even {multi}')

    else:
        found_the_max = max(l,r)

        double_the_max = found_the_max * 2

        print(f'Odd {double_the_max}')


def main(): 

    left_tines, right_tines = map(int, stdin.readline().split())

    tines_finder(left_tines, right_tines)

if __name__ == '__main__':
    main()