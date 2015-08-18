class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums:
            return False

        nums = sorted(nums)
        first = 0
        last = len(nums) - 1

        while first <= last:
            if nums[last] - nums[first] <= t and last - first <= k:
                return True
            elif nums[last] - nums[first] > t
