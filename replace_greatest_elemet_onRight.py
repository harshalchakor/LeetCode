# REPLACE ELEMENTS WITH GREATEST ELEMENT ON RIGHT SIDE. Last ELEMENT will be -1 
class Solution():
    def replace(self, nums):
        
        # First solution
        initial_max = -1
        for i in range(len(nums) -1, -1, -1):
            new_max = max(initial_max, nums[i])
            nums[i] = initial_max
            initial_max = new_max
        return nums
        
        # Second Solution
        for i in range(len(nums) - 1):
            nums[i] = max(nums[i+1:])
        nums[-1] = -1
        
        return nums
            
            
            
    
    
sol = Solution()
print(sol.replace([17,18,5,4,6,1]))
