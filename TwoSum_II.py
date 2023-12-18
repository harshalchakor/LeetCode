
# Online Python - IDE, Editor, Compiler, Interpreter
# Sorted Array is given this time [1, 3, 5, 8, 10, 13, 20]
# Using two pointer technique
class Solution:
    def TwoSumII(self, nums, target: int):
        print(nums, target)
        
        l, r = 0, len(nums) - 1
        currSum = 0
        while l < r:
            currSum = nums[l] + nums[r]
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l, r], (nums[l], nums[r])
        
sol = Solution()
print(sol.TwoSumII([1, 3, 5, 8, 10, 13, 20], 13))
