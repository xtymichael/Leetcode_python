class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
    	for i in range(len(nums)):
    		if nums[i] not in d:
    			d[nums[i]] = i
    		elif  abs(i - d[nums[i]]) <= k:
    			return True
    		else:
    			d[nums[i]] = i 
    	return False