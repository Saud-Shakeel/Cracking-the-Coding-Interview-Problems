def zeroMatrix(matrix):
    row_set, col_set = set(), set()

    for row in range(len(matrix)):
        for col in range((len(matrix[0]))):
            if matrix[row][col] == 0:
                row_set.add(row)
                col_set.add(col)

    for i in row_set:
        matrix[i] = [0] * len(matrix[0])
    
    for j in col_set:
        for j_new in range(len(matrix)):               
            matrix[j_new][j] = 0                       
                                                        
    return matrix

print(zeroMatrix([[2,0,11],[4,10,7],[9,7,1],[8,25,9]]))                      

