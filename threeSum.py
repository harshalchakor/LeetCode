# Three sum avoid duplicates 
class Answer():
    def threeSum(self, nums, target) -> int:
        
        res = []
        # nums.sort()     # this will eliminate the multiple triplets 
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:   # this will eliminate the multiple triplets 
                continue
            
            l, r = i + 1, len(nums) -1
            
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if target > threeSum:
                    l = l + 1
                elif target < threeSum:
                    r = r - 1
                else:
                    res.append([n, nums[l], nums[r]])
                    break
        return res
            
ans = Answer()
print(ans.threeSum([3, 4, 0, 1, 2, 0, 1, 2, 8], 3))
print(ans.threeSum([4, 5, 6, 7], 15))
print(ans.threeSum([55, 90, 100, 1, 90], 191))
print(ans.threeSum([36, 8, 10, 32], 76))
print(ans.threeSum([1000], 1000))
