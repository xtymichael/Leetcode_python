class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return reduce(lambda x, y: x + ' ' + y if (y != '') else x,  s.strip(' ').split(' ')[::-1])
        #easier version:
        #return " ".join(reversed(s.split()))