class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        temp = []
        for i in matrix:
        	temp += i

        first = 0
        last = len(temp) - 1
        while first <= last:
        	mid = (first + last) / 2
        	if temp[mid] == target:
        		return True
        	elif temp[mid] < target:
        		first = mid + 1
        	else:
        		last = mid - 1
        return False