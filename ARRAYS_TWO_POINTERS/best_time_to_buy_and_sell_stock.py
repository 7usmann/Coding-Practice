"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
Source: LeetCode 121
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Approach:
Use two pointers approach to track the minimum price (for buying) and calculate maximum profit as we iterate.

Time Complexity: O(n) - We iterate through the prices array once
Space Complexity: O(1) - We only use two variables regardless of input size
"""

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            # Update the minimum price if we find a lower price
            if price < min_price:
                min_price = price
            # Update maximum profit if selling at current price gives better profit
            else:
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)
                
        return max_profit

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case with profit
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    
    # Test case 2: Decreasing prices (no profit)
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    
    # Test case 3: Single price (no profit)
    assert solution.maxProfit([1]) == 0
    
    # Test case 4: Empty list
    assert solution.maxProfit([]) == 0
    
    print("All test cases passed!")