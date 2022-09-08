class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(matrix, lo, hi, target):
            
            while(lo <= hi):
                mid = lo + int((hi-lo)/2)
                
                if(target == matrix[mid]): return True
                elif(target > matrix[mid]): lo = mid+1
                else: hi = mid-1
            return False
        
        for i in range(len(matrix)):
            lo = 0
            hi = len(matrix[0])-1
            
            if(matrix[i][lo] <= target <= matrix[i][hi]):
                return binary(matrix[i], lo, hi, target)
        