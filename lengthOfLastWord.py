# Get lengthOfLastWord in a string

class Answer:
    def lengthOfLastWord(self, s) -> int:
        
        r, length = len(s) - 1 , 0
        
        while s[r] == " ":
                r -= 1
        
        while s[r] != " " and r >= 0:
                length += 1
                r -= 1
                
        return length
ans = Answer()
# here false means Prime number or True means not a prime number
print(ans.lengthOfLastWord("I am Harshal"))
print(ans.lengthOfLastWord("  Ekta is my Wife.    "))
print(ans.lengthOfLastWord("me"))   # while r >= 0  because no " " here






