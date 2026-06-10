class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        p = [[0]*(col+1) for _ in range(row+1)]
        for r in range(row):
            for c in range(col):
                p[r+1][c+1] = (matrix[r][c] + p[r][c+1] + p[r+1][c] - p[r][c])
        self.p = p
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.p
        return (p[row2+1][col2+1] - p[row1][col2+1] - p[row2+1][col1] + p[row1][col1])



# Time Complexity: O(m*n) for the constructor where m and n are the dimensions of the input matrix
# Space Complexity: O(m*n) for storing the prefix sums in the 2D array

'''
The constructor of the NumMatrix class takes a 2D input matrix and computes a 2D prefix sum array p.

The prefix sum at position (r+1, c+1) in the array p is calculated using the formula:
p[r+1][c+1] = matrix[r][c] + p[r][c+1] + p[r+1][c] - p[r][c]

This formula ensures that we are adding the current element from the original matrix and 
the prefix sums from the previous row and column, while subtracting the overlapping prefix 
sum to avoid double counting.

The sumRegion method then uses the prefix sums to calculate the sum of the elements in the 
specified region defined by (row1, col1) and (row2, col2) using the formula:
sumRegion(row1, col1, row2, col2) = p[row2+1][col2+1] - p[row1][col2+1] - p[row2+1][col1] + p[row1][col1]

This allows us to efficiently compute the sum of the specified region in constant time after 
an O(m*n) preprocessing step in the constructor.
'''