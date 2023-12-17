
# Online Python - IDE, Editor, Compiler, Interpreter
# Dynamic Programming problem.  [1, 3, 5, 0, 2, 1, 4]
# cant rob adjecent houses. Calculate what's maximum we can rob until that n. 
class Solution:
    def HouseRobber(self, nums) -> int:
        print(nums)
        rob1, rob2, maximum = 0, 0, 0
        #rob1, rob2, maximum = nums[0], nums[1], 0
        
        # [...rob1, rob2, n, n+1, ....]
        
        #for n in nums[2:]:
        for n in nums:
            maximum = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = maximum
        return rob2
        
sol = Solution()
print(sol.HouseRobber([1, 10, 5, 0, -2, 1, -4]))
