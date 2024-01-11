# How many unique paths you can reach to end of the grid[m][n] from start [0][0] position

class Answer():
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        row = [1] * n
        
        for i in range(m -1):
            newRow = [1] * n      # create new path answer row on top of old row till you create 1st row
            for j in range(n -2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
            
        return row[0]
        
ans = Answer()
print(ans.uniquePaths(3, 7)) 
print(ans.uniquePaths(4, 8)) 
print(ans.uniquePaths(1, 10))
print(ans.uniquePaths(10, 1)) 

