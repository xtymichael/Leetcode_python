class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = dict()
        for i in nums:
        	if i not in d:
        		d[i] = i
        	else:
        		return True
        return False