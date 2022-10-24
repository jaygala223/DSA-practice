class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        moves = [[0,1], [-1,0], [0,-1], [1,0]]
        
        direction = 0
        
        x, y = 0,0
        
        for c in instructions:
            if c == 'G':
                x += moves[direction][0]
                y += moves[direction][1]
            elif c == 'L':
                direction = (direction + 3) % 4
            else: direction = (direction + 1) % 4
        
        #0 is N, 1 is W, 2 is E and 3 is S
        
        return (x == 0 and y == 0) or direction