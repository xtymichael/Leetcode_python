class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i in nums:
        	if i in d:
        		d[i] += 1
        	else:
        		d[i] = 1

        length = 0
       	for j in d.keys():
       		if d[j] > 2:
       			length += 2
       		else:
       			length += d[j]

       	result = []
       	index = 0
       	for k in sorted(d.keys()):
       		if d[k] >= 2:
       			nums[index], nums[index + 1] = k, k
       			index += 2
       		if d[k] == 1:
       			nums[index] = k
       			index += 1
       	return length



################ Solution 2 ###############################
def removeDuplicates(self, nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i