class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        for i in range(1,len(prices)):
        	total_profit += max(0, prices[i] - prices[i-1]) #if today price greater then yesterday add profit
        return total_profit
