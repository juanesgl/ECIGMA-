#The last problem Kattis

from sys import stdin


def main():

   lines = stdin.readlines()


   for line in lines:
       if line.strip():
           S = line.strip()
           print(f'Thank you, {S}, and farewell!')
if __name__ == '__main__':
    main()