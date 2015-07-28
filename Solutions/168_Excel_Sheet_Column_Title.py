class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
    	result = ''
    	if n == 1:
    		return 'A'
    	while n > 0:
    		r = n % 26
    		if r == 0:
    			result += 'Z'
    		else:
    			result += chr(n % 26 + 64)
    		n -= (26**len(result))
    	return result