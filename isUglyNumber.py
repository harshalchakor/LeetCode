# The number is ugly if it's divisible by or have prime factors 2, 3, 5. 
# (Meaning division will result into 1) and no reminder. Reduce n to 1.

class Answer:
    def isUglyNumber(self, n) -> int:
        
        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p
        return n == 1
        
ans = Answer()
# here false means Prime number or True means not a prime number
print(ans.isUglyNumber(7))
print(ans.isUglyNumber(10))
print(ans.isUglyNumber(25))
print(ans.isUglyNumber(31))
print(ans.isUglyNumber(97))





