class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l = buy day, r = sell day
        maxP = 0 # track maximum profit

        while r < len(prices): 
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP



 

