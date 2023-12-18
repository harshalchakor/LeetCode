# Fibonacci sequence like
class Answer:
    def climbStairs(self, n: int) -> int:
        
        one, two = 1, 1
        
        # 1, 1, 2, 3, 5, first, second,....(n-1), n
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

ans = Answer()
print(ans.climbStairs(4))
