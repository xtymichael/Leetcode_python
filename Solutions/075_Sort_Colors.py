class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = i = 0
        right = len(nums) - 1

        while left <= right:
        	if nums[left] == 0:
        		nums[left], nums[i] = nums[i], nums[left]
        		left += 1
        		i += 1
        	elif nums[left] == 2:
        		nums[right], nums[left] = nums[left], nums[right]
        		right -= 1
        	else:
        		left += 1