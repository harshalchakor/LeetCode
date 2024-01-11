# get the length of common subsequence using dynamic programming.
class Answer():
    def wordBreak(self, text1: str, wordDict: dict) -> bool:
       
       dp = [False] * (len(text1) + 1)
       
       dp[len(text1)] = True
       
       for i in range(len(text1) -1 , -1, -1):
          for word in wordDict:
              if ((i + len(word)) <= len(text1)) and (text1[i : i+len(word)] == word):
                  dp[i] = dp[i + len(word)]
                  
              if dp[i]:
                  break
       return dp[0]

        
ans = Answer()
print(ans.wordBreak("abcde", {"abc", "de"})) 
print(ans.wordBreak("abcde", {"abcd", "ln"})) 
print(ans.wordBreak("EktaHarshalChakor", {"Chakor", "Ekta", "Harshal"})) 
print(ans.wordBreak("lmnop", {"lmno"})) 

