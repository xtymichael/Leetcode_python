class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        s = str(x)
    	while len(s) > 0:
    		if len(s) == 1:
    			return True
    		if s[0] != s[len(s)-1]: 
    			return False
    		s = s[1:len(s)-1]
    	return True