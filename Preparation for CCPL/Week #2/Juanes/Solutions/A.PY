from sys import stdin 

def main():

    A, I = map(int, stdin.readline().split())

    formula = A * (I-1) + 1

    print(formula) 

if __name__ == '__main__':
    main()