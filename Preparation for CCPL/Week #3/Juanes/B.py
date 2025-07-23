from sys import stdin 


def main():


    X = int(stdin.readline())
    N = int(stdin.readline())

    total = X * N 
    total_cost = 0

    for line in stdin:
        line = line.strip()
        if line:
            total_cost += int(line)

    avaible = total - total_cost + X 

    print(avaible)

if __name__ == '__main__':
    main()