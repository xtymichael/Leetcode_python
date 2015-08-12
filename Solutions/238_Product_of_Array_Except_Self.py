class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        product, numOfZero = self.getProduct(nums)
        for i in range(len(nums)):
        	if numOfZero == 0:       #CASE 1. NO ZERO IN LIST
        		nums[i] = product / nums[i]
        	elif numOfZero== 1:      #CASE 2. ONE ZERO IN LIST
        		if nums[i] == 0:
        			nums[i] = product
        		else:               
        			nums[i] = 0
        	else:                    #CASE 3. MORE THAN ONE ZEROES IN LIST
        		nums[i] = 0
        return nums

    def getProduct(self, nums):
    	product = 1  #product of all non zero numbers
    	numOfZero = 0 # Number of zeroes
    	for i in nums:
    		if i != 0:
    			product *= i
    		else:
    			numOfZero += 1
    	return product, numOfZero