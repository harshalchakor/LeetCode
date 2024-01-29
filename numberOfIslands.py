#Count number of islands connected by 1
class Answer():
    def numberOfIslands(self, grid):
        
        if not grid:
            return 
        
        rows, cols = len(grid), len(grid[0])
        island = 0
        
        def dfs(r, c):
            if r < 0 or r > rows-1 or c < 0 or c > cols-1 or grid[r][c] != 1:
                return
            grid[r][c] = '#'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    island = island + 1
                    
        return island
        
        
ans = Answer()

print(ans.numberOfIslands([[1, 1, 1], [1, 1, 0], [1, 0, 0]]))
print(ans.numberOfIslands([[0, 1], [1, 0]]))
print(ans.numberOfIslands([[1, 0, 1], [0, 1, 0], [0, 0, 1]]))
print(ans.numberOfIslands([[1], [0], [1]]))

'''
111
110
100

01
10

101
110
001

1
0
1
'''
