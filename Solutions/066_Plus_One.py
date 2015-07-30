class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
    	total = reduce(lambda x, y: 10 * int(x) + int(y), digits)  #can also use ''.join(listOfStrings)
    	return map(int, list(str(total + 1)))