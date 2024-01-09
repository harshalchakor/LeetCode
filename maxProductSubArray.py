class Answer():
    def maxProductSubArray(self, nums):
        
        res = max(nums)
        maxSub, minSub = 1, 1
        
        for n in nums:
            maxSub = max(n * maxSub, n * minSub, n)
            minSub = min(n * maxSub, n * minSub, n)
            
            res = max(res, maxSub)
        
        return res
    
ans = Answer()
print(ans.maxProductSubArray([2, 3, 4, 1]))
print(ans.maxProductSubArray([4, -3, 10]))
print(ans.maxProductSubArray([0, 4, -100, -5]))
print(ans.maxProductSubArray([-2, -3, 4, 1]))
