class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
    	temp = []
    	if len(s) % 2 == 1 or len(s) == 0:
    		return False
    	for i in s:
    		if i in ['[','{','(']:
    			temp.append(i)
    		else:
    			if len(temp) == 0 or {']': '[', '}': '{', ')': '('}[i] != temp[-1]:
    				return False
    			temp.pop()
    	return len(temp) == 0