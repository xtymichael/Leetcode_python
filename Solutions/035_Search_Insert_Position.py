class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
    	if not nums:
    		return 0
    	first = 0
    	last = len(nums) - 1
    	while first <= last:
    		mid = (first + last) / 2
    		if nums[mid] == target:
    			return mid
    		elif nums[mid] > target:
    			last = mid - 1
    		else:
    			first = mid + 1
    	return first
