class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[i] == target:
                return True
        return False



