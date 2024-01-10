class Answer():
    def maxContainerWater(self, nums) -> int:
        
        maxArea = 0
        l, r = 0, len(nums) - 1
        
        while l < r:
            currArea = (r - l) * min(nums[l], nums[r])
            maxArea = max(maxArea, currArea)
            
            if nums[r] > nums[l]:
                l = l + 1
            else:
                r = r -1
                
        return maxArea
    
ans = Answer()

print(ans.maxContainerWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))
