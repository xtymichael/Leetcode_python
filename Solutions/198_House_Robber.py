# f(0) = nums(0)
# f(1) = max(nums(0), nums[1])
# f(k) = max(f(k-2) + nums(k), f(k-1))


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
        	last, now = now, max(last + i, now)
        return now