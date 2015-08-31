class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
        	return False
        if num == 1:
        	return True
        if num % 5 == 0:
        	return self.isUgly(num / 5)
        if num % 3 == 0:
        	return self.isUgly(num / 3)
        if num % 2 == 0:
        	return self.isUgly(num / 2)
        return False
        

###################### Solution 2##################
class Solution(object):
    def isUgly(self, num):
        for p in 2, 3, 5:      ### gettinr rid of all 2s, then all 3s, then all 5s
            while num % p == 0 < num: 
                num /= p
        return num == 1