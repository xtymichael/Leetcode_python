class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
    	numOfZero = 0
    	start = 5
    	while start <= n:
    		numOfZero += n / start
    		start = start * 5
    	return numOfZero


######## numOfZero = floor(n/5) + floor(n/25) + .....#####