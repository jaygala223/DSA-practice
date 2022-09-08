class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])
        lo = 0
        hi = n-1
        
        while(lo <= hi):
            mid = lo + int((hi-lo)/2)
            
            max_row = 0
            for i in range(len(mat)):
                if(mat[max_row][mid] < mat[i][mid]):
                    max_row = i
            
            if (mid == n-1 or mat[max_row][mid+1]< mat[max_row][mid]) and (mid == 0 or mat[max_row][mid] > mat[max_row][mid-1]):
                return [max_row, mid]
            
            elif mid>0 and mat[max_row][mid] < mat[max_row][mid-1]:
                hi = mid-1
            else: lo = mid+1
                
        return [-1,-1]