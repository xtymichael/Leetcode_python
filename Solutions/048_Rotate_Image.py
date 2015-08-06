class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        dim = len(matrix)
        copy = [x[:] for x in matrix] ### copy = matrix is wrong since they point to the same thing
        if dim > 1:
	        for i in range(dim):
	        	for j in range(dim):
	        		matrix[i][j] = copy[dim - j - 1][i]

