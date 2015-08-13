class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if not s or len(s) == 1:
        	return s
        for i in range(len(s) - 1, 0, -1):
        	if s[:i][::-1] == s[:i]:
        		s = s[i:] + s
        		return s

