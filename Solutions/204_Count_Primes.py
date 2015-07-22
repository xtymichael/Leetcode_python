class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        # n = 0 1 2 case
        if (n == 0 or n == 1 or n == 2):
            return 0
        
        # n > 2 case
        isPrime = [False] * n
        for l in range(2,n):
            isPrime[l] = True
        
        for i in range(2,n):
            if (i * i > n or not isPrime[i]):
                continue
            for j in xrange(i * i, n, i):
                isPrime[j] = False

        return isPrime.count(True)