#Kattis Statistics 

from sys import stdin

def main():
    case = 1
    for line in stdin:
        data = list(map(int, line.strip().split()))
        nums = data[1:]  
        minimum = min(nums)
        maximum = max(nums)
        tha_range = maximum - minimum
        print(f'Case {case}: {minimum} {maximum} {tha_range}')
        case += 1

if __name__ == '__main__':
    main()

    