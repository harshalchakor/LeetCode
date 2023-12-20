# you can take 1 index jump or 2 index jump and that much ot will cost.

class Answer:
    def minCostClimbing(self, costs) -> int:
        # [10, 15, 20] 0
        costs.append(0)
        
        for i in range(len(costs) - 3, -1, -1):
            costs[i] = min(costs[i] + costs[i+1], costs[i] + costs[i+2])
        return min(costs[0], costs[1])
            
                    
ans = Answer()
print(ans.minCostClimbing([10, 15, 20]))
print(ans.minCostClimbing([10, 15, 20, 100, 1]))
print(ans.minCostClimbing([101, 15, 20, 100, 1]))







