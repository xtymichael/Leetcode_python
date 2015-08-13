class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s or s[::-1] == s:
        	return s
        
        for i in range(1, len(s)):
        	for j in range(i + 1):
        		temp = s[j:(len(s)-1-(i-j))]
        		if temp == temp[::-1]:
        			return temp
        		

 