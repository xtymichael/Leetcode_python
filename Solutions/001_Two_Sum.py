class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = dict()
        
        for i in range(len(nums)):
            key = target - nums[i]
            if key in d:
                return [d[key] + 1, i + 1]
            else:
                d[nums[i]] = i
        return []