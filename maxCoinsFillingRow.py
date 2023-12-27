# How many maximum ballons from the given text you can spell? 

import collections

class Answer:
    def maxCoinsFillingRow(self, n) -> int:
        
        # max number of rows we can fill using 'n' coins are n or less than n
        l, r = 1, n
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            coins = (mid * (mid + 1)) / 2
            
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid) 
        return res
        
ans = Answer()
print(ans.maxCoinsFillingRow(20))
print(ans.maxCoinsFillingRow(1))
print(ans.maxCoinsFillingRow(3))
print(ans.maxCoinsFillingRow(0))

