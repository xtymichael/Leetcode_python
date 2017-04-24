class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        head = ''
        tail = ''

        for char in s:
        	if char not in d or d[char] == 0:
        		d[char] = 1
        	elif d[char] == 1:
        		d[char] = 0
        		head = head + char
        		tail = char + tail
        if sum(d.values()) != 0:
        	return len(head + tail) + 1
        return len(head + tail)





------------------------------------------
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = sum(v & 1 for v in collections.Counter(s).values()) 
        #count how many letters appear an odd number of times

        return len(s) - odds + bool(odds)

