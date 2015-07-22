class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        total = 0
        while len(s) > 0:
            total = total * 26 + ord(s[0].upper()) - 64
            s = s[1:]
        return total