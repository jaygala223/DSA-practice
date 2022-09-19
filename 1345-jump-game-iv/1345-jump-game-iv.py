class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 0
        
        #number --> indexes
        indexes = defaultdict(list)
        
        for i in range(len(arr)):
            indexes[arr[i]].append(i)
        
        queue = [0]
        ans = 0
        visited = set()
        visited.add(0)
        
        while queue:
            for i in range(len(queue)):
                
                currIdx = queue.pop(0)
                
                if currIdx == n-1: return ans
                
                nextPos = currIdx + 1
                prevPos = currIdx - 1
                mirrors = indexes[arr[currIdx]]

                if prevPos >= 0 and prevPos < n and prevPos not in visited:
                    visited.add(prevPos)
                    queue.append(prevPos)

                if nextPos < n and nextPos >= 0 and nextPos not in visited:
                    visited.add(nextPos)
                    queue.append(nextPos)

                for val in mirrors:
                    if val >= 0 and val < n and val not in visited:
                        visited.add(val)
                        queue.append(val)
                del indexes[arr[currIdx]]
            
            ans += 1
            
        return ans
            