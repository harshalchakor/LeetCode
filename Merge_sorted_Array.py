# merge num2 into num1 with sorted

class Answer:
    def mergeSortedArray(self, num1, m, num2, n):
        
        last_index_num1 = m + n -1
        
        # compare reverse order and fill num1 from last index
        while m > 0 and n > 0:
            if num1[m - 1] > num2 [n - 1]:
                num1[last_index_num1] = num1[m - 1]
                m -= 1
            else:
                num1[last_index_num1] = num2[n - 1]
                n -= 1
            last_index_num1 -= 1 
        
        if n > 0:
            num1[last_index_num1] = num2[n-1]
            n, last_index_num1 = n-1, last_index_num1 -1
            
        return num1

ans = Answer()
print(ans.mergeSortedArray([1, 5, 7, 0, 0, 0, 0], 3, [1, 2, 6, 8], 4))
