from sys import stdin

def main():
   
    N = int(stdin.readline().strip())
    
    alturas_globos_str = stdin.readline().strip().split()
    
    alturas_globos = [int(alturas_globos_str[i]) for i in range(min(N, len(alturas_globos_str)))]
    
    arrow_counter = 0
    balonis_height = {}
    
    for altura_globo in alturas_globos:
       
        if altura_globo in balonis_height and balonis_height[altura_globo] > 0:
         
            balonis_height[altura_globo] -= 1
          
            nueva_altura_flecha = altura_globo - 1
            if nueva_altura_flecha > 0:
                balonis_height[nueva_altura_flecha] = balonis_height.get(nueva_altura_flecha, 0) + 1
        else:
            
            arrow_counter += 1
            nueva_altura_flecha = altura_globo - 1
            if nueva_altura_flecha > 0:
                balonis_height[nueva_altura_flecha] = balonis_height.get(nueva_altura_flecha, 0) + 1
    
    print(arrow_counter)

if __name__ == "__main__":
    main()