from sys import stdin


def cuadrants_checker(x,y):

    if x > 0 and y > 0:
        print(f'1')
    elif x < 0 and y > 0:
        print(f'2')
    elif x < 0 and y < 0:
        print(f'3')
    elif x > 0 and y < 0:
        print(f'4')
     
def main():

    x = int(stdin.readline())
    y = int(stdin.readline())

    cuadrants_checker(x,y)

if __name__== '__main__':
    main()