# convert the 2D or 3D grid into single array idx postions and then shift by k value.

class Answer():
    def shiftGrid(self, grid, k: int):
        rows, columns = len(grid), len(grid[0])
        
        # converting grid position to single array index
        def posToIndex(r, c):
            return ((r * columns) + c)               # idx
            
        # converting array index to grid position (r, c)
        def indexToPos(idx):
            return ((idx // columns), (idx % columns))    # r, c
        
        res = [[0] * columns for i in range(rows)]
            
        # Go through each position and find the new position after shifting by k value
        for r in range(rows):
            for c in range(columns):
                idx = posToIndex(r, c)
                newIdx = (idx + k) % (rows * columns)
                newRow, newColumn = indexToPos(newIdx)
                res[newRow][newColumn] = grid[r][c]
                
        return res
        
        
ans = Answer()

print(ans.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))
print(ans.shiftGrid([[10, 20], [30, 40]], 1))
print(ans.shiftGrid([[5, 6, 7, 8]], 1))
print(ans.shiftGrid([[]], 1))
