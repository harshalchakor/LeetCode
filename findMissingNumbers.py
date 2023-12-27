#find the missing numbers in range [1, n]

class Answer:
    def findMissingNumbers(self, nums):
        
        hashset = set()
        res = []
        
        for i in range(1, len(nums) + 1):
            hashset.add(i)
        # print(hashset)
        for n in nums:
            if n in hashset:
                hashset.remove(n)
                
        # return hashset
        
        for n in hashset:
            res.append(n)
        return res
            

ans = Answer()
print(ans.findMissingNumbers([1, 2, 5, 3, 6, 4, 4]))
print(ans.findMissingNumbers([1, 2, 6, 3, 6, 6, 7]))
print(ans.findMissingNumbers([1, 4, 6, 11, 6, 6, 7, 0]))
print(ans.findMissingNumbers([11]))
