class Answer():
    def maxProductSubArray(self, nums):
        
        res = max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            res = max(res, curMax)
        
        return res
    
ans = Answer()
print(ans.maxProductSubArray([2, 3, 4, 1]))
print(ans.maxProductSubArray([4, -3, 10]))
print(ans.maxProductSubArray([0, 4, -100, -5]))
print(ans.maxProductSubArray([-2, -3, 4, 1]))
