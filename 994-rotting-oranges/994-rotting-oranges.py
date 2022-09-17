class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        
        if rows == 0: return -1
        
        cols = len(grid[0])
        
        #fresh oranges
        freshCount = 0
        
        rotten = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add rotten orange location to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    freshCount += 1
        
        minutes = 0
        
        while freshCount>0 and rotten:
            minutes += 1
            
            for _ in range(len(rotten)):
                
                x,y = rotten.pop(0)
                
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    newX, newY = x + dx, y + dy
                    
                    if newX < 0 or newX == rows or newY < 0 or newY == cols:
                        continue
                    
                    if grid[newX][newY] == 2 or grid[newX][newY] == 0:
                        continue
                        
                    freshCount -= 1
                    
                    grid[newX][newY] = 2
                    
                    rotten.append((newX, newY))
                    
        return minutes if freshCount == 0 else -1
                