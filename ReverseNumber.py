class Answer:
    def ReverseNumber(self, n: int) -> int:
        MIN = -2147483648 # -2^31
        MAX = 2147483648. # 2^31
        
        res = 0
        while n:   # 123
            digit = int(n % 10)  #3
            n = int(n / 10) #12
            if (res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10)): # 214748364 or 3 > 8
                return -1
            if (res < MIN // 10 or (res == MIN // 10 and digit > MIN % 10)):
                return -1
                
            # shift previously added digit to the right by * 10 and add new digit
            res = (res * 10) + digit
        return res
        
# Output
ans = Answer()
print(ans.ReverseNumber(1234))
