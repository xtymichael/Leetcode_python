class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        first = 0
        last = len(nums) - 1
        if len(nums) == 1:
        	return 0

        while first < last - 1:
        	mid = (first + last) / 2
        	if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
        		return mid
        	elif nums[mid] < nums[mid + 1]:
        		first = mid + 1
        	else:
        		last = mid - 1
        		
        return first if nums[left] > nums[right] else last
        	