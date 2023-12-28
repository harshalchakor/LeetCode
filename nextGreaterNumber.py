
# num2 is subarray of num1. Print the next greter element of each element from num2 looking in num1. 
# if not found add -1

class Answer:
    def nextGreaterNumber(self, num1, num2):
        
        num2index = {}
        res = [-1] * len(num2)
        
        for i, n in enumerate(num2):
            num2index[n] = i
        
        for i in range(len(num1)):
            if num1[i] in num2index:
                for j in range(i+1, len(num1)):
                    if num1[j] > num1[i]:
                        idx = num2index[num1[i]]
                        res[idx] = num1[j]
                        break
        
        return res
        
ans = Answer()
print(ans.nextGreaterNumber([7, 1, 5, 3, 6, 4], [3, 1, 4]))
print(ans.nextGreaterNumber([30, 2, 11, 9, 22, 57], [30, 2, 57, 9]))
