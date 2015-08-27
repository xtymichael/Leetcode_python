class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        start = 0
        end = len(nums) - 1

        if start == end:
        	return nums
        else:
        	for i in range(len(nums)):
        		swap(nums[i], nums[start])
        		permute(nums[start+1:])
        		swap(nums[i], nums[start])

	def swap(a, b):
		a, b = b, a