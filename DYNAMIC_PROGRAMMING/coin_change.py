"""
Problem: Coin Change
Difficulty: Medium
Source: LeetCode 322
URL: https://leetcode.com/problems/coin-change/

Description:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Approach:
Use dynamic programming to build up the solution. For each amount from 0 to the target,
calculate the minimum number of coins needed.

Time Complexity: O(amount * n) where n is the number of coin denominations
Space Complexity: O(amount) for the dp array
"""

class Solution:
    def coinChange(self, coins, amount):
        # Initialize dp array with amount + 1 (which is larger than any possible result)
        # dp[i] represents the minimum coins needed to make amount i
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0
        
        # Build up the dp array
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still amount + 1, it means we couldn't make the amount
        return dp[amount] if dp[amount] <= amount else -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Standard case
    assert solution.coinChange([1, 2, 5], 11) == 3
    
    # Test case 2: No solution
    assert solution.coinChange([2], 3) == -1
    
    # Test case 3: Zero amount
    assert solution.coinChange([1, 2, 5], 0) == 0
    
    # Test case 4: Single coin denomination equals amount
    assert solution.coinChange([1], 5) == 5
    
    print("All test cases passed!")