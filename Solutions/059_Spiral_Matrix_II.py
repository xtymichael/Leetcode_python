class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for x in range(n)] for x in range(n)]
        i, j, di, dj = 0, 0, 0, 1

        for k in range(n*n):
        	result[i][j] = k + 1
        	if result[(i+di)%n][(j+dj)%n]: #right turn if next number exists
        		di, dj = dj, -di
        	i += di
        	j += dj
        return result
