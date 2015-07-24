class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        r = ''
        if x < 0:
        	x = -x
        	r += '-'
        for i in range(len(str(x))):
        	r += str(x)[len(str(x))-i-1]

        if int(r) > 2**31-1 or int(r) < -2**31:
        	return 0
        return int(r)


#####MY SOLUTION DID NOT TAKE INPUT SUCH AS '+123' INTO ACCOUNT#########


#####BETTER SOLUTION#######################
# class Solution:
#     # @param {integer} x
#     # @return {integer}
# 	def reverse(self, x):   
# 	    string = str(abs(x))
# 	    result=int(string[::-1])
# 	    if x < 0:
# 	    	result = - result
# 	    if -2**31 <= result <= 2**31 - 1:
# 	    	return result
# 	    return 0