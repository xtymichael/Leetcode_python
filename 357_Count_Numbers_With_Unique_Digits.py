#https://leetcode.com/discuss/107945/java-dp-o-1-solution
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
        	return 0
        if n == 0:
        	return 1

        answer = 10  #basic case when n == 1
        unique_digits = 9
        available_digits = 9
        while n > 1:
        	unique_digits *= available_digits #new number of uniques
        	answer += unique_digits # add it to last total number
        	available_digits -= 1
        	n -= 1
        return answer
