def check_parity(matrix):

    n = len(matrix)
    row_errors = []
    col_errors = []

    for i in range(n):
        row_sum = sum(matrix[i])
        if row_sum % 2 != 0:
            row_errors.append(i)
    
  
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum % 2 != 0:
            col_errors.append(j)
    
    if not row_errors and not col_errors:
        return "OK" 
    elif len(row_errors) == 1 and len(col_errors) == 1:
        return f"Change bit ({row_errors[0] + 1},{col_errors[0] + 1})"  
    else:
        return "Corrupt"  


def main():
   
    n = int(input())
    
   
    if n > 0:
        
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        
    
        result = check_parity(matrix)
        print(result)


if __name__ == "__main__":
    main()