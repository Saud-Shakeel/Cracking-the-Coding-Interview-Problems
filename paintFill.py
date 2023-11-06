def paintFill(grid, i, j, new_col, old_col):
   
    if grid[i][j] == old_col:
        grid[i][j] = new_col

        
        if j < len(grid[0]) - 1:
            paintFill(grid, i, j + 1, new_col, old_col)
        if j > 0:
            paintFill(grid, i, j - 1, new_col, old_col)
            
        if i < len(grid) - 1:
            paintFill(grid, i + 1, j, new_col, old_col)
        if i > 0:
            paintFill(grid, i - 1, j, new_col, old_col)
     
    

grid = [[1, 2, 3], [4, 2, 6], [2, 2, 9]]
paintFill(grid, 2, 0, 10, 2)

print(grid)




