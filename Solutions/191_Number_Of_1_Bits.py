class Solution:
# @param n, an integer
# @return an integer
	def hammingWeight(self, n):
		sum = 0
		while n:
			sum += n&1  #and logic: ex: n = 8(1000 base 2)     sum += 1000 & 0001
			n /= 2
		return sum