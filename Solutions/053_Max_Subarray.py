class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for i in nums[1:]:
            curSum = max(i, curSum + i)
            maxSum = max(curSum, maxSum)
        return maxSum
