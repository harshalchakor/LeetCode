class Answer:
    def ReplaceElementWithMaxRight(self, nums):
        # Maxright is -1
        # iterate reverse 
        # newMax = max(oldmax, nums[i])
        
        maxRight = -1
      
        for i in range(len(nums) -1, -1, -1):
            newMax = max(maxRight, nums[i])
            nums[i] = maxRight
            maxRight = newMax
          
        return nums

ans = Answer()
print(ans.ReplaceElementWithMaxRight([1,20, 7, 6, 8, 1, 4]))
