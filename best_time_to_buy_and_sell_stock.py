class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) == 0:
            return 0
        
        minprice = prices[0]
        maxprofit = 0
        
        for price in prices:
            # minprice changes when everytime a lower price shows
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
            
        return maxprofit