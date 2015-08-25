class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        if len(sum) < 4 or sum(nums[:4]) > target or sum(nums[-4:]) < target:
            return []


        