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
    
ans = Answer()
print(ans.MejorityElement([1, 6, 6, 4, 5, 5, 5]))
