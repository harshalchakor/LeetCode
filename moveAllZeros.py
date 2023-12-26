# move all zeros to the right of aaray

class Answer():
    
    def moveAllZeros(self, nums):
        l = 0
        
        for r in range(len(nums)):
            if nums[r]:                                # non-zero element
                nums[l], nums[r] = nums[r], nums[l]    # swap r non-zero value with l's 0 value
                l += 1
        
        return nums
    
ans = Answer()
print(ans.moveAllZeros([0, 2, 0, 8, 9, 0, 24, 26]))
