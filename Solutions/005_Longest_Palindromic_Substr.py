class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        i ,l = 0, 0
        for j in range(len(s)):
            if j - l >= 0 and s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
        return s[i: i+l]