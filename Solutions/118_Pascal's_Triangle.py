class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
    	result = [[] for j in range(numRows)]
    	for i in range(numRows):
    		for j in range(i+1):
    			result[i].append(self.fact(i)/(self.fact(j)*self.fact(i-j)))
    	return result

    def fact(self,n):
    	if n == 1 or n == 0:
    		return 1
    	return n*self.fact(n-1)
        