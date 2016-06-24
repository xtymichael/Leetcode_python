class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d = dict()
        bulls = 0
        cows = 0

        for char in secret:
        	if char not in d:
        		d[char] = 0
        	d[char] += 1

        for char in guess:
        	if char in d and d[char] > 0:
        		cows += 1
        		d[char] -= 1

        for t in zip(secret, guess):
        	if t[0] == t[1]:
        		cows -= 1
        		bulls += 1

        return str(bulls) + 'A' + str(cows)+'B'
