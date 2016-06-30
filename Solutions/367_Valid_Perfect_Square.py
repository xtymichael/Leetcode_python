class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
        	return False

        first = 0
        last = num
        while first <= last:
        	mid = first + (last - first) / 2
        	if mid * mid == num:
        		return True
        	elif mid * mid > num:
        		last = mid - 1
        	else:
        		first = mid + 1
        return False

