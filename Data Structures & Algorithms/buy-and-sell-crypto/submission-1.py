"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
Input: prices = [10,1,5,6,7,1]

Output: 6

lowest_price_seen = prices[0]
res = 0
for prices in range (1,n):
    res = max(res, prices[i] - lowest_prices_seen)
    lowest_price_seen = min(lowest_price_seen,prices[0])
    

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lowest_price_seen = prices[0]
        res = 0
        for i in range (1,n):
            res = max(res, prices[i] - lowest_price_seen)
            lowest_price_seen = min(lowest_price_seen, prices[i])
        return res
                