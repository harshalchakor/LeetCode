# Reverse integer on 32bit scale.
class Answer():
    def coinChange(self, coins, amount) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for amt in range(1, amount+1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1+ dp[amt - coin])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
                
ans = Answer()
print(ans.coinChange([1, 3, 4, 5], 7))
print(ans.coinChange([1, 2, 3], 3))
print(ans.coinChange([5, 10, 3, 2], 20))
print(ans.coinChange([5, 10, 3], 24))
print(ans.coinChange([5, 7, 3], 4))

