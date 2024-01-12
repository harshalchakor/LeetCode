# Can you jump to the end of array using nums?

class Answer():
    
    def insertInterval(self, intervals, newInterval):
        
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        
        return res
        
        
ans = Answer()
print(ans.insertInterval([[1, 3], [6, 7]], [4, 5])) 
print(ans.insertInterval([[1, 3], [6, 8], [9, 10]], [2, 7])) 
print(ans.insertInterval([[5, 7], [7, 10]], [1, 3]))
print(ans.insertInterval([[1, 3], [6, 7]], [8, 10]))
print(ans.insertInterval([[1, 3], [4, 6], [8, 11]], [2, 9])) 

