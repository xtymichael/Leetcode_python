class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        return len(s.strip(' ').split(' ')[-1])