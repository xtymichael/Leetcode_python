class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
        	return len(nums)

        maxLength = 0
        d = dict()

        for i in nums:
        	if i not in d:
        		right = d[i + 1] if i + 1 in d else 0  # num of items on the right side of this number
        		left = d[i - 1] if i - 1 in d else 0 	# num of items on the left side of this number
        		d[i] = left + right + 1 # length = (num of left + middle + num of right)

        		maxLength = max(maxLength, left + right + 1) #update maxLen

        		d[i + right] = d[i - left] = left + right + 1 #updtae bondary dict length

        return maxLength