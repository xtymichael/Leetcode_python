###########      R U L E S    ######3####
# The function first discards as many whitespace characters (as in isspace) as necessary 
#until the first non-whitespace character is found. Then, starting from this character, 
#takes an optional initial plus or minus sign followed by as many base-10 digits as possible, 
#and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, 
# which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, 
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed and zero is returned.


class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
    	result = 0
    	sign = 1
    	
    	if len(str) == 0:
    		return 0

    	while str.find(' ') == 0: #gettring rid of whitespace in the front
    		str = str[1:]

    	first = str[0]     #get the sign
    	if first == '-':
    		sign = -1
    		str = str[1:]
    	if first == '+':
    		sign = 1
    		str = str[1:]

    	for i in range(len(str)): #turn into int
    		if str[i].isdigit():
    			result = 10*result + (ord(str[i]) - 48)
    		else:
    			break
    	
    	result  = result * sign    #return the final result
    	if  result > 2**31-1:
    		return 2**31 - 1
    	elif result < -2**31:
    		return -2**31
    	else:
    		return result









