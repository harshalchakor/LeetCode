# Remove duplicates and find the unique integers in array

class Answer:
    def removeDuplicates(self, nums) -> int:
        l = 1
        count = {}                      # n: frequency
        for r in range(1, len(nums)):
            if nums[r] != nums[r -1]:
                nums[l] = nums[r]
                l += 1
            else:
                count[nums[r]] = 1 + count.get(nums[r], 1)
                
        print(count)                    # frequency of duplicate numbers   
        return l                        # Number of unique integers
        
ans = Answer()
print(ans.removeDuplicates([2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 7]))



