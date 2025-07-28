from sys import stdin 


def main():

    word = stdin.readline().strip()

    if 'ss' in word:
        print('hiss')
    else:
        print('no hiss')

if __name__ == '__main__':
    main()