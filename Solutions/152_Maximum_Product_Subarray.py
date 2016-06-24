class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_product = neg_product = max_product = nums[0]

        for num in nums[1:]: #go thru remaining elements in nums
        	a = pos_product * num 
        	b = neg_product * num #b can be positive if num is negative

        	pos_product = max(max(a,b), num) #max(a,b) is positive product
        	neg_product = min(min(a,b), num) #min(a,b) is negative product
        	max_product = max(max_product, pos_product) #update max product

        return max_product


