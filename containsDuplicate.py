# Number of 1 bits in integer number
class Answer():
    def containsDuplicate(self, nums) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return False
            hashset.add(n)
        return True
            
                
ans = Answer()
print(ans.containsDuplicate([1, 2, 3, 4, 5, 6, 6]))
print(ans.containsDuplicate([1, 2, 3, 4, 5, 6, 8]))
