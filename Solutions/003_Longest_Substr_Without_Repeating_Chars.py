class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
    	start = maxLength = 0
    	usedChar = dict()

    	for i in range(len(s)):
    		if s[i] in usedChar and start <= usedChar[s[i]]:
    			start = usedChar[s[i]] + 1
    		else:
    			maxLength = max(maxLength, i - start + 1)

    		usedChar[s[i]] = i

    	return maxLength





