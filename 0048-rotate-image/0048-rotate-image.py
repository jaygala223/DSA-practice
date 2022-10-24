class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        matrix.reverse()
        
        for i in range(rows):
            for j in range(i+1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return matrix
        