# move all zeros to the right of aaray

class Answer():
    
    def findPivotIndex(self, nums) -> int:
        
        totalsum = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = totalsum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
        
ans = Answer()
print(ans.findPivotIndex([1, 18, 1, 15, 4]))
print(ans.findPivotIndex([100, 50, 1, -100, -50, 300]))
print(ans.findPivotIndex([2, 0, 0]))
print(ans.findPivotIndex([-1,-1,0,1,1,0]))
