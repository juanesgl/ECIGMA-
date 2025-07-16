#Kattis Statistics 

from sys import stdin 

def main():
    
    case = 1
    
    for line in stdin:
        x = map(int, stdin.readline().split)
        minimum = min(x)
        maximum = max(x)
        tha_range = maximum - minimum

        print(f'Case {case}: {minimum}{maximum}{tha_range}')
        case+=1


if __name__ == '__main__':
    main()

    