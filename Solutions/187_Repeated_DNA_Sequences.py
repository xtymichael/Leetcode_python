class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
        	return []
        result = []
        d = dict()
        for i in range(len(s) - 9):
        	seq = s[i: i+10]
        	if seq in d and seq not in result:
        		result.append(seq)
        	else:
        		d[seq] = 1
        return result


