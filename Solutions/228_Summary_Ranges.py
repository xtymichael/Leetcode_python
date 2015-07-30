class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        temp = []   #String[]
        result = [] #String[]
        if not nums:
            return []
        for i in range(len(nums)):
            if not temp or int(temp[-1]) + 1 == nums[i]:
                temp.append(str(nums[i]))
            else:
                result.append(self.getRange(temp))
                temp = [str(nums[i])]
            if i == len(nums) - 1:
                result.append(self.getRange(temp))
        return result

    def getRange(self, temp):
        if len(temp) == 1:
            return temp[0]
        else:
            return temp[0] + '->' + temp[-1]