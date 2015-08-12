########################   Recursion    ##################
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n/2)




########################   Iterative     ##################
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1/x
            n = -n
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            else:
                x *= x
                n /= 2
        return result

