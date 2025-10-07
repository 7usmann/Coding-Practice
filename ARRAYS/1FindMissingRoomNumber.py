"""
Problem: 1FindMissingRoomNumber
Difficulty: Easy
Source: Custom (similar to LeetCode 268 - Missing Number)

Description:
A hotel has n rooms numbered from 0 to n. Due to a system glitch, when guests check in,
one room number was not registered in the system. Given an array of integers representing the
room numbers that were registered, find the one missing room number.

Note: The room numbers are in the range [0, n] and each room appears exactly once in the array except for the missing room.

Example 1:
Input: rooms = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number.

Example 2:
Input: rooms = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number.

Example 4:
Input: rooms = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number.

Approach:
There are several ways to solve this problem:
1. Math formula: Sum of numbers from 0 to n is n*(n+1)/2, subtract the sum of the array from this
2. HashSet: Put all numbers in a set, then check which number from 0 to n is not in the set
3. XOR: Using the property that a^a = 0 and a^0 = a, XOR all numbers from 0 to n and all numbers in the array
"""

class Solution:
    def findMissingRoom(self, rooms):
        rooms.sort()

        for v in range(len(rooms)):
            if rooms[v] != v:
                return v
        
        if rooms[-1] != len(rooms):
            return len(rooms)
        
# return sum(range(len(rooms)+1)) - sum(rooms)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Missing number in the middle
    rooms1 = [3, 0, 1]
    print(f"Test case 1: Missing room = {solution.findMissingRoom(rooms1)}")
    assert solution.findMissingRoom(rooms1) == 2
    
    # Test case 2: Missing number at the end
    rooms2 = [0, 1]
    print(f"Test case 2: Missing room = {solution.findMissingRoom(rooms2)}")
    assert solution.findMissingRoom(rooms2) == 2
    
    # Test case 3: Missing number in a larger array
    rooms3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"Test case 3: Missing room = {solution.findMissingRoom(rooms3)}")
    assert solution.findMissingRoom(rooms3) == 8

    
    # Test case 4: Edge case - smallest possible array
    rooms4 = [0]
    print(f"Test case 4: Missing room = {solution.findMissingRoom(rooms4)}")
    assert solution.findMissingRoom(rooms4) == 1

    
    # Test case 5: Edge case - missing the first number
    rooms5 = [1, 2, 3]
    print(f"Test case 5: Missing room = {solution.findMissingRoom(rooms5)}")
    assert solution.findMissingRoom(rooms5) == 0
    
    print("All test cases passed!")