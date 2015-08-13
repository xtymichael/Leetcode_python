class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x < 0:
        	return None
        first = 1
        last = x
        while first != last - 1:
        	mid = (first + last) / 2
        	square = mid * mid
        	if square == x:
        		return mid
        	elif square > x:
        		last = mid
        	else:
        		first = mid
        return first



####https://leetcode.com/discuss/23945/my-python-solution-cost-77ms