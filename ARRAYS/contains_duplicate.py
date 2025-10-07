"""
Problem: Contains Duplicate
Difficulty: Easy
Source: LeetCode 217
URL: https://leetcode.com/problems/contains-duplicate/

Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true
Input: nums = [1,2,3,4]
Output: false

Approach:
Use a hash set to keep track of seen numbers. If we encounter a number that's already in the set, return True.

Time Complexity: O(n) - We iterate through the array once
Space Complexity: O(n) - In the worst case, we store all elements in the set
"""

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Contains duplicate
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    
    # Test case 2: No duplicates
    assert solution.containsDuplicate([1, 2, 3, 4]) == False
    
    # Test case 3: Multiple duplicates
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    
    print("All test cases passed!")