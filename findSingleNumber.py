# Find single number which is not come twice in array

class Answer():
    
    def findSingleNumber(self, nums) -> int:
        
        res = 0
        
        for n in nums:
            res = res ^ n         # XOR operation removes duplicates
        return res
                
ans = Answer()
print(ans.findSingleNumber([1, 18, 1, 18, 1]))
print(ans.findSingleNumber([-100, 50, 1, -100, 50, 1, 50]))
print(ans.findSingleNumber([2, 0, 0]))
print(ans.findSingleNumber([-1, 1, -1, 1, 3, -1, 3]))
