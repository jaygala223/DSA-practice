class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        zeros = []
        
#         for i in range(len(arr)):
#             if arr[i] == 0:
#                 zeros.append(i)
        
        
        visited = {}
        
        def jumps(ind):
            if ind < 0 or ind >= len(arr):
                return False
            
            if ind in visited and visited[ind] >= 2: return False
            
            if arr[ind] == 0:
                return True
            
            #visited cnt ++
            visited[ind] = 1 + visited.get(ind, 0)
            
            return jumps(arr[ind] + ind) or jumps(ind - arr[ind])
        
        return jumps(start)