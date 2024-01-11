# No adjecent houses can be robbed and array is circular meaing last and first num are adjecent
class Answer():
    
    def houseRobberII(self, nums) -> int:
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]), nums[0])
        
    def helper(self, nums):
        rob1, rob2 = 0, 0
            
        # [...rob1, rob2, n, n+1,...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
            
        
ans = Answer()
print(ans.houseRobberII([1, 2, 3, 4, -5])) #[2, 4]
print(ans.houseRobberII([3, -4, 1, 6, 8, 0])) #[3, 1, 8]
print(ans.houseRobberII([-1, 4, 10, -5, -7])) #[10]
print(ans.houseRobberII([5])) 

