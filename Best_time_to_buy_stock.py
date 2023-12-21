class Answer:
    def maxProfit(self, prices) -> int:
        l, r = 0, 1
        maxProfit = 0
        
        while r < len(prices):
            if prices[r] > prices[l]:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)
            else:
                l = r
            r += 1
            
        return maxProfit

ans = Answer()
print(ans.maxProfit([7, 1, 5, 3, 6, 4]))
