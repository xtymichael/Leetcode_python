class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
    	i = 0
    	j = len(s) - 1
    	s = s.lower()
    	while j > i:
    		if not (s[i].isalpha() or s[i].isdigit()):
    			i += 1
    			continue
    		if not (s[j].isalpha() or s[j].isdigit()):
    			j -= 1
    			continue
    		if s[j] != s[i]:
    			return False
    		i += 1
    		j -= 1
    	return True
