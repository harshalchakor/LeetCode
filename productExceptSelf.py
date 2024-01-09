class Answer():
    def productExceptSelf(self, nums):
        
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix = prefix * nums[i]
            
        # print(res)
            
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = postfix * res[i]
            postfix = postfix * nums[i]
        
        return res
    
ans = Answer()
print(ans.productExceptSelf([2, 3, 4, 5]))
print(ans.productExceptSelf([4, -3, 10]))
print(ans.productExceptSelf([0, 4, 100, 5, 6]))
print(ans.productExceptSelf([2, 3, 4, 1]))
