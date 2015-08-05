class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
    	MAX_INT = 2 ** 31 - 1
    	sign = 1
    	result = 0
        if divisor == 0:
        	return 0
        if divisor == 1:
        	return dividend
        if divisor == -1:
        	return -dividend
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
        	sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
        	result += 1
        	dividend -= divisor
        return min(MAX_INT,sign * result)



