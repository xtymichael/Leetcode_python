class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        cur = 2
        for i in range(n):
            cur =