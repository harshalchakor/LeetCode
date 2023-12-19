# when the squares of the digits == 1 then Happy number 
class Answer:
    def HappyNumber(self, n: int) -> bool:
        
        repeat = set()
        
        while n not in repeat:
            repeat.add(n)
            n = self.squaresum(n)
            if n == 1:
                print(repeat)
                return True
        return False
            
    def squaresum(self, n: int) -> int:
        Output = 0
        while n:
            digit = n % 10
            Output = Output + digit ** 2
            n = n // 10
        return Output

ans = Answer()

# Output

print(ans.HappyNumber(23))
