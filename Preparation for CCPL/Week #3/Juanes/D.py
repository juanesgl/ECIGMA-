from sys import stdin 


def main():

    people, dr_chaz = map(int, stdin.readline().split())

    if dr_chaz > people:
        leftovers = dr_chaz - people

        if leftovers == 1:
            print(f'Dr. Chaz will have 1 piece of chicken left over!')

        else:
            print(f'Dr. Chaz will have {leftovers} pieces of chicken left over!')

    else:
        needed = people - dr_chaz

        if needed == 1:
            print(f'Dr. Chaz needs 1 more piece of chicken!')

        else:
            print(f'Dr. Chaz needs {needed} more pieces of chicken!')

if __name__ == '__main__':
    main()