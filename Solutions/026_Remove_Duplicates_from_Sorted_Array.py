class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
    	d = dict()
    	i = 0
    	while i < len(nums):
    		if nums[i] in d:
    			nums.pop(i)
    			#after pop, i does not change since len(nums) changed
    		else:
    			d[nums[i]] = nums[i]
    			i += 1

    	return len(nums)
