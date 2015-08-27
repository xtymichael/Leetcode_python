class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
        	return ''
        return reduce(self.getPrefix, strs)
    def getPrefix(self, s1, s2):
    	i = 0
    	while i < len(s1) and i < len(s2):
    		if s1[i] == s2[i]:
    			i += 1
    		else:
    			break
    	return s1[:i]
