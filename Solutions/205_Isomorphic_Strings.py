class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
    	d1 = dict()
    	d2 = dict()

    	if len(s) != len(t):
    		return False

    	for i in range(len(s)):
    		if s[i] not in d1:
    			d1[s[i]] = [i]
    		else:
    			d1[s[i]].append(i)

    		if t[i] not in d2:
    			d2[t[i]] = [i]
    		else:
    			d2[t[i]].append(i)

    	for j in range(len(s)):
    		if d1[s[j]] != d2[t[j]]:
    			return False

    	return True
    		



#################### USE ZIP(S,T) IS EASIER########################