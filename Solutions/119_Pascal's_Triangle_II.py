class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
    	result = []
    	for i in range(rowIndex+1):
    		result.append(self.fact(rowIndex)/(self.fact(i) * self.fact(rowIndex - i)))
    	return result

    def fact(self,n):
    	if n == 0 or n == 1:
    		return 1
    	return self.fact(n-1) * n