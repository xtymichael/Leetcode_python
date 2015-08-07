# Returns a pointer to the first occurrence of str2 in str1, or a null pointer if str2 is not part of str1.

# The matching process does not include the terminating null-characters, but it stops there.

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
    	if not needle:
    		return 0
    	i = 0
    	for j in range(len(haystack)):
    		if haystack[j] == needle[i] and len(haystack[j:]) >= len(needle):
    			temp = j
    			while i <= len(needle) - 1:
    				if haystack[temp] == needle[i] and i == len(needle) - 1:
    					return j
    				elif haystack[temp] == needle[i]:
    					temp += 1
    					i += 1
    				else:
    					i = 0
    					break
    	return -1
    	


################# Way more efficient solution #############
    def strStr(self, haystack, needle):
        l1 = len(needle)
        l2 = len(haystack)
        for i in xrange(l2 - l1 + 1):
            if needle == haystack[i:i + l1]:
                return i
        return -1