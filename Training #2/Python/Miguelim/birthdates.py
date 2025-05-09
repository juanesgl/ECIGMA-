from sys import stdin
from datetime import date

def solve(datas,dic):
    maxim = max(datas) 
    minum = min(datas)
    
    mn = [clave for clave, valor in dic.items() if valor == maxim]
    nn = [clave for clave, valor in dic.items() if valor == minum]

    return *mn, *nn

def main():

    n = int(stdin.readline().strip())
    datas = []
    dic = dict()

    for _ in range(n):
        line = stdin.readline().strip().split()
        dic[line[0]] = date(int(line[3]), int(line[2]), int(line[1]))
        datas.append(date(int(line[3]), int(line[2]), int(line[1])))
    
    soly, solo = solve(datas, dic)
    print(soly)
    print(solo)

main()
