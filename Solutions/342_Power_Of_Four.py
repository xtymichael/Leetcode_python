class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # power of four have even number of zeroes after 1
        # 00&11 = 0 (num & 3 == 0)
        while num > 0 and num & 3 == 0:
            num >>= 2
        return num == 1

    
