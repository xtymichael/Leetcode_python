class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        if not nums:
        	return False

        first = 0
        last = len(nums) - 1

        while first <= last:
        	mid = (first + last) / 2
        	if nums[mid] == target:
        		return True
        	elif nums[mid] == nums[last]:
        		last -= 1
        	elif nums[mid] == nums[first]:
        		first += 1
        	elif (nums[mid] < target <= nums[last]) or (target <= nums[last] < nums[mid]) or (nums[last] < nums[mid] < target):
        		first = mid + 1
        	else:
        		last = mid - 1

        return False