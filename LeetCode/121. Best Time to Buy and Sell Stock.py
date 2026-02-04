from lc import *
# ============================================================
# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ============================================================


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total, minP = 0, inf
        for p in prices:
            total = max(total, p - minP)
            if p < minP: minP = p
        return total


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max(a - b for a, b in zip(prices, accumulate(prices, min)))


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return max(map(sub, prices, accumulate(prices, min)))


test("""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104


""")
