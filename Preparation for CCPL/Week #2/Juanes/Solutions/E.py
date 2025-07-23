from sys import stdin

def main():
    
    TC = int(stdin.readline()) 

    for _ in range(TC):  
        n = int(stdin.readline())  
        calculation = (((((n * 567) // 9) + 7492) * 235) // 47) - 498
        residual = abs(calculation) // 10 % 10
        print(residual)

if __name__ == '__main__':
    main()
