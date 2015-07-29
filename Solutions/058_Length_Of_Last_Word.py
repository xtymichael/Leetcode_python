class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        return s.strip(' ').split(' ')[-1]