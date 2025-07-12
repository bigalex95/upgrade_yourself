"""
LeetCode Problem: 1. Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums, target):
        """
        Find indices of two numbers that add up to target
        
        Args:
            nums: List[int] - Array of integers
            target: int - Target sum
            
        Returns:
            List[int] - Indices of the two numbers
        """
        # Create a hash map to store values and their indices
        num_map = {}  # value -> index
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # If complement exists in our map, we found our answer
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, add current number to the map
            num_map[num] = i
            
        # No solution found (though problem states there is always one)
        return []


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    result = solution.twoSum(nums, target)
    print(f"Test 1: nums={nums}, target={target}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {sorted(result) == sorted(expected)}\n")
    
    # Test case 2
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    result = solution.twoSum(nums, target)
    print(f"Test 2: nums={nums}, target={target}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {sorted(result) == sorted(expected)}\n")
    
    # Test case 3
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    result = solution.twoSum(nums, target)
    print(f"Test 3: nums={nums}, target={target}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {sorted(result) == sorted(expected)}\n")


if __name__ == "__main__":
    test_solution()
