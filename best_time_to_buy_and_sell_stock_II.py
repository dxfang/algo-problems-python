class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
            
        return sum(prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i-1])