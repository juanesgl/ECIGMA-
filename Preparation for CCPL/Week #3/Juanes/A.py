from sys import stdin 


def main():
    
    TC = int(stdin.readline())
    qaly = 0
    for _ in range(0,TC):
        q, y = map(float, stdin.readline().split())
        qaly += q*y

    print(qaly) 
if __name__ == '__main__':
    main()