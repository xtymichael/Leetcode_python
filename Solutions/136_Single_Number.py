class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d.pop(nums[i])
            else:
                d[nums[i]] = nums[i]
        
        if len(d) == 1:
            return d.keys()[0]
        else:
            return []