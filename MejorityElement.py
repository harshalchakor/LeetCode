# return the number with max count
class Answer:
    def MejorityElement(self, nums) -> int:
        count = {}     # n --> count
        maxCount = 0
        res = nums[0]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            maxCount = max(maxCount, count[n])
            res = n if  maxCount > count[res] else res
        return res
        
        # Solution 2. Only will work when element is occured more than half times the length of array. 
        
        count, res = 1, nums[0]
        
        for n in nums:
            if count == 0:
                res = n
            count = (count + 1) if n == res else (count - 1)
        return res
    
ans = Answer()
print(ans.MejorityElement([1, 6, 6, 4, 5, 5, 6, 6]))
