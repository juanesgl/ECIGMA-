from sys import stdin



def main():

    X,Y = map(int, stdin.readline().split())

    if X == 0 and Y == 1:
        print(f'ALL GOOD')
    elif Y == 1:
        print(f'IMPOSSIBLE')
    else:

        formula = X/(1 - Y)

        print(round(formula,6))

if __name__== '__main__':
    main()