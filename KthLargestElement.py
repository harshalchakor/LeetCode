import heapq
class KthLargestElement():
    def __init__(self, nums, k: int):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        print(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        print(self.minheap)
            
    def add(self, value: int) -> int:
        heapq.heappush(self.minheap, value)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
                
ans = KthLargestElement([100, 2, 300, 4, 5, 6, 600, 1], 3)
print(ans.add(20))
print(ans.add(50))
print(ans.add(700))


