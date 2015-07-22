class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n == 1 or ( n != 0 and n % 2 == 0 and self.isPowerOfTwo(n/2))