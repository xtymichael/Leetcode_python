class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
    	d = dict()
        for i in range(len(nums)):
        	if nums[i] not in d:
        		d[nums[i]] = 0

    		l = d[nums[i]] + 1
    		if l > len(nums) / 2:
    			return nums[i]
    		d[nums[i]] = l



############################################
# BEST SOLUTION############################

# def majorityElement(nums):
#         return sorted(nums)[len(nums)/2]