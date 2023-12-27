# How many maximum ballons from the given text you can spell? 

import collections

class Answer:
    def isPerfectSquare(self, num) -> int:
        
        # for i in range(1, num + 1):
        #     if i * i == num:
        #         return True, i
        #     if i * i > num:
        #         return False
                
        l, r = 1, num
        
        while l <= r:
            mid = (l + r) // 2
            if (mid * mid) > num:
                r = mid -1
            elif (mid * mid) < num:
                l = mid + 1
            else:
                return True, mid
        return False
       
        
ans = Answer()
print(ans.isPerfectSquare(100))
print(ans.isPerfectSquare(7))
print(ans.isPerfectSquare(81))
print(ans.isPerfectSquare(16))
print(ans.isPerfectSquare(26))

