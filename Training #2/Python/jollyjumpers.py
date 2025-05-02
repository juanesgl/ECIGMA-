from sys import stdin as sd

def jolly_or_not_jolly(listd):

    n = len(listd)
    if n == 1:
        return "Jolly"
    else:
        m = max(listd[1:])
        suma = sum(listd) - listd[0]
        suma_2 = (m*(m + 1)) >> 1 #(n*(n+1)) / 2
        if (suma == suma_2): 
            return "Jolly" 
        else:
            return "Not Jolly" 
        
def main():
   
    line = sd.readline().strip()

    while line != "":

        lists = [int(x) for x in line.split()]
        listd = []

        for i in range(1, len(lists)):
            listd.append(abs(lists[i] - lists[i - 1]))

        print(jolly_or_not_jolly(listd))
        line = sd.readline().strip()

main()