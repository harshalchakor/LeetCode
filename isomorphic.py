# create two maps for each of two string characters
class Answer():
    def isomorphic(self, s, t) -> bool:
        mapST, mapTS = {}, {}
        
        if len(s) != len(t):
            return False
        
        for s1, t1 in zip(s, t):
            if (s1 in mapST and mapST[s1] != t1) or (t1 in mapTS and mapTS[t1] != s1):
                return False
            mapST[s1] = t1
            mapTS[t1] = s1
        return True
                
                
ans = Answer()
print(ans.isomorphic("aabbaa", "eettee"))
print(ans.isomorphic("aabbaa", "ffzzfz"))
print(ans.isomorphic("aabbcct", "ddccwwt"))
