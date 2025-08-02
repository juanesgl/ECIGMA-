from sys import stdin 

def main():
    TC = int(stdin.readline())
    for _ in range(TC):
        just_one_case = stdin.readline().strip()
        if just_one_case == 'P=NP':
            print('skipped')
        else:
            a, b = map(int, just_one_case.split('+'))
            print(a + b)

if __name__ == "__main__":
    main()
