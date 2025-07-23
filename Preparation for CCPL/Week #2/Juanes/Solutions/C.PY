from sys import stdin

def main():
    e_miles = float(stdin.readline().strip())
    romani_pace = e_miles * 1000 * 5280 / 4854
    print(f'{round(romani_pace)}')

if __name__ == '__main__':
    main()
