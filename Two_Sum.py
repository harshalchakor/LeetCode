
# Online Python - IDE, Editor, Compiler, Interpreter

class Solution:
    def TwoSum(self, nums, target: int):
        print(nums, target)
        
        preMap = {} #index : num
        for i, n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i]
            else:
                preMap[n] = i
        return

sol = Solution()
print(sol.TwoSum([1, 2, 3, 5, 7, 8], 8))
