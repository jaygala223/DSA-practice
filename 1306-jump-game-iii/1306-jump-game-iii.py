class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = {}
        
        def jumps(ind):
            if ind < 0 or ind >= len(arr):
                return False
            
            if ind in visited: return False
            
            if arr[ind] == 0:
                return True
            
            #visited cnt ++
            visited[ind] = 1
            
            return jumps(arr[ind] + ind) or jumps(ind - arr[ind])
        
        return jumps(start)