# Create stack (LIFO) with queue(FIFO)

class stack:
    
    def __init__(self):
        self.q = deque()
        
    def push(self, x: int) -> None:
        self.q.append(x)
        
    def top(self) -> int:
        return self.q[-1]
        
    def pop(self) -> int:    
        for i in range(len(self.q) - 1):      # only do below steps till second last value. Last value we need.  
            self.push(self.q.popleft())       # remove element from queue's left and add/append to right till second last value
        return self.q.popleft()               # return the last stored queue value
        
    def empty(self):
        return len(q) == 0
        
        
        
