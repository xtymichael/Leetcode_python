class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if not rows:
            return []
        cols = len(matrix[0])
        result = []
        i = j = 0
        if cols > 1:
            di, dj = 0, 1
        else:
            di, dj = 1, 0
        visited =[[0 for x in range(cols)] for y in range(rows)]
        for k in range(rows*cols):
            result.append(matrix[i][j])
            visited[i][j] = 1
            if visited[(i+di)%rows][(j+dj)%cols]:
                di, dj = -dj, di
            i += di
            j += dj
        return result

