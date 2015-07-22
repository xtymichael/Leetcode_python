class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        temp = []
        while n != 1:
            if n in temp:
                return False
            temp.append(n)
            n = self.getNewNumber(n)
        return True

    def getNewNumber(self,a):
        new = 0
        while a > 0:
            r = a - a/10*10
            a = a/10
            new = new + r*r
        return new