# Palindrom if one character deleted?  

class Answer():
    def charDelpalindrome(self, word: str) -> bool:
        l, r = 0, len(word) -1
        
        while l < r:
            if word[l] != word[r]:
                skipL = word[l + 1: r + 1]   # delete or skip the left char
                skipR = word[l:r]            # delete or skip the right char
                return ((skipL == skipL[::-1]) or      # check if the substrings are palindrom
                          (skipR == skipR[::-1]))
            l, r = l + 1, r - 1
            
        return True
        
    
ans = Answer()

print(ans.charDelpalindrome("aba"))
print(ans.charDelpalindrome("acbdca"))
print(ans.charDelpalindrome("tacbca"))
print(ans.charDelpalindrome("pwewewetpwewewe"))
print(ans.charDelpalindrome("nitinp"))
