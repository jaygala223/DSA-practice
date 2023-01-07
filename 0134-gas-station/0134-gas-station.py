class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        total = 0
        ansIdx = 0
        
        diff = 0
        
        for i in range(0, n):
            diff += gas[i] - cost[i]    
            total += gas[i] - cost[i]
            
            if(total < 0):
                total = 0
                ansIdx = i+1
                
        if diff<0:
            return -1 
        else: return ansIdx