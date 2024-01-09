# Find minimum number in the Rotated Sorted array.
class Answer():
    def searchNumRotatedArray(self, nums, target) -> int:
        
        l, r = 0, len(nums) -1
        
        while l <= r:
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # left sorted portion meaning your mid is max value
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion meaning your mid is min value
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
ans = Answer()
print(ans.searchNumRotatedArray([3, 4, 0, 1, 2], 0))
print(ans.searchNumRotatedArray([4, 5, 6, 7], 7))
print(ans.searchNumRotatedArray([55, 90, 100, 1], 55))
print(ans.searchNumRotatedArray([36, 8, 10, 32], 9))
print(ans.searchNumRotatedArray([1000], 1000))
