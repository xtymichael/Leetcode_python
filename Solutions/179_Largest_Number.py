class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = map(str, num)
        num.sort(lambda x, y: cmp(y+x, x+y))
        return ''.join(num).lstrip('0') or '0'
