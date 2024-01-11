# in array of 1 to n, count the number of 1 bits in that every number of array. 
class Answer():
    def countingBits(self, n):
        
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
                
            dp[i] = 1 + dp[i - offset]
            
        return dp
                
ans = Answer()
print(ans.countingBits(3))
print(ans.countingBits(7))
print(ans.countingBits(8))
print(ans.countingBits(16))
print(ans.countingBits(31))
