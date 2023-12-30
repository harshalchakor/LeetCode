
class Answer:
    def reverseString(self, text: str) -> str:
        
        # solution 1
        
        print(text[::-1])
        
        # solution 2
        
        arr = list(text.lower().split())  # keeping the complete word then reversing
        print(" ".join(arr[::-1]))
        
        # solution 3
         
        arr = list(text.lower())    # converts string into array
        l, r = 0, len(arr) - 1
        while l < r:
            arr[l] , arr[r] = arr[r], arr[l]   # reverse the array positions
            l = l + 1
            r = r - 1
        print("".join(arr))      # convert array to string again
        
        # solution 4: keeping the complete word then reversing
        
        arr = list(text.lower().split())
        def reverse(l, r):
            if l < r:
                arr[l] , arr[r] = arr[r], arr[l]  # reverse the array positions
                reverse(l + 1, r - 1)
        reverse(0, len(arr) - 1)
        return (" ".join(arr))
        
        
        
ans = Answer()
print(ans.reverseString(". hi My name is  & 123Harshal458 1"))

