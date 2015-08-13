class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0] or not target or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row, col =  len(matrix), len(matrix[0])
        if row == col == 1:
            return matrix[0][0] == target
        first = 0
        last = row * col - 1
        mid = (first + last) / 2
        cur = matrix[mid/col][mid%col]
        if cur == target:
            return True
        elif cur > target:
            if matrix[0][mid%col] <= target:
                matrix = [[x[mid%col] for x in matrix[:(mid/col)]]]

            else:
                matrix = [x[:(mid%col + 1)] for x in matrix[:(mid/col + 1)]]
        else:
            if matrix[-1][mid%col] >= target:
                matrix = [[x[mid%col] for x in matrix[(mid/col + 1):]]]
            else:
                matrix = [x[(mid%col):] for x in matrix[(mid/col):]]
        return self.searchMatrix(matrix, target)