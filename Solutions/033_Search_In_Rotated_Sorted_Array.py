class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
    	first = 0
    	last = len(nums) - 1
    	while first <= last:
    		mid = (first + last) / 2
    		if nums[mid] == target:
    			return mid
    		elif (target <= nums[last] < nums[mid]) or (nums[mid] < target <= nums[last]) or (nums[last] < nums[mid] < target):
    			first = mid + 1
    		else:
    			last = mid - 1
    	return -1
