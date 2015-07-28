class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
    	temp = []   #String[]
    	result = [] #String[]
    	if len(nums) == 0:
    		return []
    	if len(nums) == 1:
    		return [str(nums[0])]
        for i in range(len(nums)):
        	if temp == []:
        		temp.append(str(nums[i]))
        	elif int(temp[-1]) + 1 == nums[i]:
        		temp.append(str(nums[i]))
        	elif i == len(nums) - 1:
        		result.append(self.getRange(temp))
        		result.append(str(nums[i]))
        	else:
        		result.append(self.getRange(temp))
        		temp = []
        return result

    def getRange(self, temp):
    	if len(temp) == 0:
    		return None
    	if len(temp) == 1:
    		return temp[0]
    	else:
    		return temp[0] + '->' + temp[-1]