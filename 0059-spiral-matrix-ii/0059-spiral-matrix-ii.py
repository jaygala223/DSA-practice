class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        start_row = 0
        end_row = n-1
        start_col = 0
        end_col = n-1
        
        
        # arr = [[0]*n]*n
        
        arr = [[0 for i in range(n)] for j in range(n)]
        
        if n == 0: return matrix
        
        num = 1
        
        while start_row <= end_row and start_col <= end_col:
            
            for i in range(start_col, end_col+1):
                arr[start_row][i] = num
                num += 1
            
            start_row += 1
            
            for i in range(start_row, end_row+1):
                arr[i][end_col] = num
                num += 1
            
            end_col -= 1
        
            for i in range(end_col, start_col-1, -1):
                if start_row <= end_row:
                    arr[end_row][i] = num
                    num += 1

            end_row -= 1
        
            for i in range(end_row, start_row-1, -1):
                if start_col <= end_col:
                    arr[i][start_col] = num
                    num += 1
            
            start_col += 1
            
        return arr
        