class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        if not nums:
        	return []
        d = dict()
        for i in nums:
        	if i in d:
        		d.pop(i, None)
        	else:
        		d[i] = i
        return d.keys()
