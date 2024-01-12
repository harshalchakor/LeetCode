# Can you jump to the end of array using nums?

class Answer():
    
    def canJump(self, nums) -> bool:
        
        dest = len(nums) - 1
        
        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= dest:
                dest = i
                
        return True if dest == 0 else False
        
        
ans = Answer()
print(ans.canJump([4,2,1,7])) 
print(ans.canJump([3, 2, 1, 0, 8])) 
print(ans.canJump([1, 3, 0, 0, 1, 0]))
print(ans.canJump([0, 1, 1, 1, 4])) 

