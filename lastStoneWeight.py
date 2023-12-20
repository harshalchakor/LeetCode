# Smash maximum stone weights each time and get the last stone weight

class Answer:
    def lastStoneWeight(self, stones) -> int:
        
        stones = [-s for s in stones]            # [-2, -3, -4, -5, -6]
        heapq.heapify(stones)                    # [-6, -5, -4, -3, -2] 
                                                # minheap: top of the stack will be min value
        
        while len(stones) > 1:
            
            first_big_stone = heapq.heappop(stones)   # -6
            second_big_stone = heapq.heappop(stones)  # -5
            if second_big_stone > first_big_stone: # if weight differs then calculate diff and add to heap
                heapq.heappush(stones, first_big_stone - second_big_stone)
        
        stones.append(0)
        return abs(stones[0])
        
        
        
ans = Answer()
print(ans.lastStoneWeight([2, 3, 4, 5, 6]))



