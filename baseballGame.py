# count the score with symballs 

class Answer():
    def baseballGame(self, nums) -> int:
        
        stack = []
        
        for c in nums:
            if c == "+":
                stack.append(stack[-1] + stack[-2])
            elif c == "D":
                stack.append(2*stack[-1])
            elif c == "C":
                stack.pop()
            else:
                stack.append(int(c))
                
        return sum(stack)
        
        
ans = Answer()

print(ans.baseballGame(["5", "2", "C", "D", "+"]))
print(ans.baseballGame(["5", "D", "C", "3", "D", "+"]))
print(ans.baseballGame(["1", "D", "+", "D", "C", "3", "4"]))
print(ans.baseballGame(["20", "C", "5", "7", "+", "D", "4"]))
print(ans.baseballGame(["20", "30", "40", "C", "C", "D"]))
print(ans.baseballGame([]))
