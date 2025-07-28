from sys import stdin 

def relational_algebra(a,b):
    if a < b: print(f'<')
    elif a > b: print(f'>')
    else: print(f'=')

def main():

    TC = int(stdin.readline())


    for _ in range(TC):
        a, b = map(int, stdin.readline().split())

        relational_algebra(a,b)    
if __name__ == '__main__':
    main()