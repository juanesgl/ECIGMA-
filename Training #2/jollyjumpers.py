from sys import stdin as sd


def jolly_or_not_jolly(listd):
    
    suma = sum(listd)

    n = listd[1]

    suma_2 = (n*(n - 1)) >> 1 #(n*(n+1)) / 2

    if suma == suma_2:

        print('Jolly')
        
    else:
        print('Not Jolly')

    


def main():
   
    
    line = sd.readline().strip()
    while line != 0:

        lists = [int(x) for x in line.split()]
        listd = []

        for i in range(0, len(lists), 2):
            
            listd.append(abs(lists[i] - lists[i - 1]))

        
        jolly_or_not_jolly(listd)

        line = sd.readline().strip()



main()