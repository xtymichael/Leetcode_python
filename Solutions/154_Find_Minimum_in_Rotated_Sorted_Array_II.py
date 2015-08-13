class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        first = 0
        last = len(nums) - 1
        while first < last:
        	mid = (first + last) / 2
        	if nums[mid] == nums[last]:
        		last -= 1
        	elif nums[mid] > nums[last]:
        		first = mid + 1
        	else:
        		last = mid
        return nums[first]
