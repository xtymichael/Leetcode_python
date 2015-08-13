class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums:
        	return [-1, -1]
        
        result = [-1, -1]

        first = 0
        last = len(nums) - 1
        
        while first <= last:
        	mid = (first + last) / 2
        	if nums[mid] == target:
        		result[1] = mid
        		first = mid + 1
        	elif nums[mid] > target:
        		last = mid - 1
        	else:
        		first = mid + 1


        left = 0
        right = len(nums) - 1
        while left <= right:
        	mid = (left + right) / 2
        	if nums[mid] == target:
        		result[0] = mid
        		right = mid - 1
        	elif nums[mid] > target:
        		right = mid - 1
        	else:
        		left = mid + 1

        return result