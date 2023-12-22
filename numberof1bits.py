# Number of 1 bits in integer number
class Answer():
    def numberof1bits(self, n: int) -> int:
        ans = 0
        while n:
            ans += n % 2
            n = n >> 1
        return ans
        
        # solution 2
        
        ans = 0
        while n:
            n = n & (n - 1)
            ans += 1
        return ans
        
                
ans = Answer()
print(ans.numberof1bits(7))
print(ans.numberof1bits(5))
print(ans.numberof1bits(509))
