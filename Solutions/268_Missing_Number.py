class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        return (1 + l) * l / 2 - sum(nums) 

################# Solution 2 ##################


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (set(range(len(nums) + 1)) - set(nums)).pop()