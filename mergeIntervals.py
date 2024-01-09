class Answer():
    def mergeIntervals(self, intervals):
        
        # intervals.sort(key = lambda i : i[0])
        intervals.sort()                        # by default it will sort on first index
        # print(intervals)
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            
            if output[-1][1] >= start:                    # lastEnd = output[-1][1]  last elements 1st index
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
                
        return output
    
ans = Answer()
print(ans.mergeIntervals([[1, 6], [9, 11], [11, 13], [14, 15], [2, 5]]))
print(ans.mergeIntervals([[1, 6], [5, 8], [9, 15]]))
print(ans.mergeIntervals([[1, 5], [4, 8], [6, 7]]))
print(ans.mergeIntervals([[2, 3], [4, 5], [8, 5], [6, 12]]))
