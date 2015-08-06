class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
    	while val in nums:
    		nums.remove(val)
    	return len(nums)