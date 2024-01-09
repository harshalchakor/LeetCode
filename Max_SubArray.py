
# Online Python - IDE, Editor, Compiler, Interpreter

class Solution:
    def MaxSubArray(self, nums) -> int:
        print(nums)
        left = 0
        maxSub = nums[0]
        currSum = 0
        for i, n in enumerate(nums):
            if currSum < 0:
                currSum = 0
                left = i
            currSum += n
            right = i
            maxSub = max(maxSub, currSum)
        return maxSub, nums[left:right]

sol = Solution()
print(sol.MaxSubArray([-1, -3, 5, 8, 8, -20]))
