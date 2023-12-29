
class Answer:
    def BinarySearch(self, nums, target):
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2    # if (l + r) is out of bounds for int then l + (r -l) will work the same
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
        
        
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
            
        
        
ans = Answer()
print(ans.BinarySearch([7, 1, 5, 3, 6, 4], 6))
print(ans.BinarySearch([30, 2, 11, 9, 22, 57], 5))
