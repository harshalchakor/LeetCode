# search number and return index, if not found then return index where it will be inserted

class Answer:
    def searchInsertNumber(self, nums, target) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
ans = Answer()
print(ans.searchInsertNumber([1, 2, 4, 5, 6], 6))
print(ans.searchInsertNumber([1, 2, 4, 5, 6], 3))
print(ans.searchInsertNumber([2], 3))
print(ans.searchInsertNumber([2], 1))


