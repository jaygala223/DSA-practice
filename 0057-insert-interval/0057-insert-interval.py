class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        s, e  = newInterval[0], newInterval[1]
        
        for i in range(len(intervals)):
            #current waale ke peeche hai
            if e < intervals[i][0]:
                ans.append([s,e])
                return ans + intervals[i:]
            
            #current waale ke aage hai
            elif s > intervals[i][1]:
                ans.append(intervals[i])
                
            #overlapping
            else:
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
        
        ans.append([s,e])
        return ans