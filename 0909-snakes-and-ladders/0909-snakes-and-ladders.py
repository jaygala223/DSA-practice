class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        arr = [0]
        moves = 0
        n = len(board)**2
        visited = set()
        q = [1]
        
        for i, row in enumerate(board[::-1]): arr += row[::-1] if i%2 else row
        
        #bfs
        while q:
            level = []
            
            for curr in q:
                if curr == n: return moves
                for i in range(1, 7):
                    if curr + i <= n and curr + i not in visited:
                        visited.add(curr + i)
                        level.append(curr + i if arr[curr + i] == -1 else arr[curr + i])
            q = level
            moves += 1
        return -1