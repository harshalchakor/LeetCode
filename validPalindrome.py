class Answer():
    def isPalindrome(self, s) -> bool:
        
        l, r = 0, len(s) -1
        
        while l < r:
            while l < r and not self.isalphnum(s[l]):
                l = l + 1
            while r > l and not self.isalphnum(s[r]):
                r = r - 1
            if s[l].lower() != s[r].lower():
                return False
            
            l = l + 1
            r = r - 1
        return True
    
    def isalphnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') 
                or ord('a') <= ord(c) <= ord('z') 
                or ord('1') <= ord(c) <= ord('9'))
                
ans = Answer()
print(ans.isPalindrome("    aabbaa"))
print(ans.isPalindrome("    aabbaa     "))
print(ans.isPalindrome("    aabtbaa"))
print(ans.isPalindrome(" +   aabt. &tbaa   -  "))
print(ans.isPalindrome("    aabbcaa     "))
