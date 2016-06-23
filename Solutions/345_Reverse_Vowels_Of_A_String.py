class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = list(s)
        vowel = 'aeiouAEIOU'
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
        	if word[p1] in vowel and word[p2] in vowel:
        		word[p1], word[p2] = word[p2], word[p1]
        		p1 += 1
        		p2 -= 1

        	if word[p1] not in vowel:
        		p1 += 1

        	if word[p2] not in vowel:
        		p2 -= 1

        return ''.join(word)