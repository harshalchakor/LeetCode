
# Online Python - IDE, Editor, Compiler, Interpreter

class Solution:
    def anagram(self, s: str, t: str) -> bool:
        print(s, t)
        
        if len(s) != len(t):
            return False
            
        mapS, mapT = {}, {}
        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        print(mapS, mapT)
        
        if mapT != mapS:
            return False
        return True

sol = Solution()
print(sol.anagram("abaatb", "abaabt"))
