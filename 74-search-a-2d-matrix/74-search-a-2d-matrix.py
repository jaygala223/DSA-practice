class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0])-1
        
        while(j >= 0 and i < len(matrix)):
            if(matrix[i][j] == target): return True
            
            if(matrix[i][j] < target): i+=1
            else: j-=1
        return False
        