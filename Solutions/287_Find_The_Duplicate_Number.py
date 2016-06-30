class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        total = 0
        i = 0
        while i < len(nums):
            total += i
        return sum(nums) - total
