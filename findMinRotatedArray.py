# Find minimum number in the Rotated Sorted array.
class Answer():
    def findMinRotatedArray(self, nums):
        res = nums[0]
        l, r = 0, len(nums) -1
        
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2 
            res = min(res, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
            
    
ans = Answer()
print(ans.findMinRotatedArray([3, 4, 0, 1, 2]))
print(ans.findMinRotatedArray([4, 5, 6, 7]))
print(ans.findMinRotatedArray([55, 90, 100, 1]))
print(ans.findMinRotatedArray([36, 8, 10, 32]))
print(ans.findMinRotatedArray([1000]))
