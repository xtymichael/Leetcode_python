class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        while num > 9:
            s = 0
            while num > 0:
                s += num%10
                num /= 10
            num = s
        return num