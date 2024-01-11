# get the length of common subsequence using dynamic programming.
class Answer():
    def LongestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # creating 2D matrix with 0 values
        
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i +1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i+1][j]) 
        
        return dp[0][0]
       
        
ans = Answer()
print(ans.LongestCommonSubsequence("abcde", "ace")) 
print(ans.LongestCommonSubsequence("abcde", "abcde")) 
print(ans.LongestCommonSubsequence("abcde", "efghi")) # only 'e' match
print(ans.LongestCommonSubsequence("pqr", "lmn")) # nothing match

