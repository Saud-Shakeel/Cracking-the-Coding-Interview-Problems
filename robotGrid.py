def robotGrid(arr,i,j):
    if arr[i][j] == 1:
        return True
    
    if arr[i][j] == -1:
        return False
    
    if i< len(arr[0])-1:
        return robotGrid(arr, i+1, j)
    if j< len(arr[0])-1:
        return robotGrid(arr, i, j+1)
    
grid = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

print(robotGrid(grid, 0, 0))