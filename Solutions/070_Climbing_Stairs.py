class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
    	total = 0
    	if n == 0 or n == 1 or n == 2:
    		return n
    	if n % 2 == 0:
    		numOfTwos = n/2
    		numOfOnes = 0
    		while n > -2:
    			total += self.fact(numOfOnes + numOfTwos) / (self.fact(numOfTwos) * self.fact(numOfOnes))
    			numOfOnes += 2
    			numOfTwos -= 1
    			n = n - 2
    	else:
    		numOfTwos = n/2
    		numOfOnes = 1
    		while n > -1:
    			total += self.fact(numOfOnes + numOfTwos) / (self.fact(numOfTwos) * self.fact(numOfOnes))
    			numOfOnes += 2
    			numOfTwos -= 1
    			n = n - 2
    	return total

    def fact(self,a):
    	if a == 0:
    		return 1
    	else:
    		return a * self.fact(a-1)