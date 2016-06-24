class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
        	return 0
        min_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
        	min_price = min(min_price, p)
        	max_profit = max(max_profit, p - min_price)
        return max_profit
