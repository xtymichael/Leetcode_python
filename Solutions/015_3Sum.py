class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
    	d = dict()
    	result = []

    	for i in nums:
    		if i not in d:
    			d[i] = 1
    		else:
    			d[i] += 1

    	sortD = d.keys()
    	for j in range(len(sortD)):
    		first = sortD[j]
    		d[first] -= 1
    		for k in range(j, len(sortD)):
    			second = sortD[k]
    			if d[second] > 0:
    				d[second] -= 1
    			else:
    				continue
    			third = - (first + second)
    			temp = sorted([first, second, third])
    			if third in sortD and d[third] > 0 and temp not in result:
    					result.append(temp)
    			d[second] += 1
    		d[first] += 1
    	return result




###########################################################################
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) <3: # deal with special input
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]


        nums = sorted(nums) # sorted, O(nlgn)
        ans = []

        for i in range(len(nums) -2):
            j = i+1
            k = len(nums) -1 # hence i < j < k

            while j<k: # if not cross line
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    ans.append((nums[i], nums[j], nums[k]))

                if temp_sum > 0: # which means we need smaller sum, move k backward, remember we sort the array
                    k -= 1
                else:
                    j += 1

        return list(set(tuple(ans))) # I bet this is not the best way to eliminate duplicate solutions
