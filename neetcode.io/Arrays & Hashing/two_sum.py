"""
Two Sum
LeetCode #1: https://leetcode.com/problems/two-sum/
NeetCode: https://neetcode.io/problems/two-integer-sum

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to the target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices whose values sum to target
        """
        num_to_index = {}  # stores number -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        
        return []  # in case no solution is found (problem statement guarantees one)


def test_two_sum():
    """Test cases for Two Sum problem"""
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    result1 = solution.twoSum(nums1, target1)
    assert sorted(result1) == sorted(expected1), f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    result2 = solution.twoSum(nums2, target2)
    assert sorted(result2) == sorted(expected2), f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    result3 = solution.twoSum(nums3, target3)
    assert sorted(result3) == sorted(expected3), f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    expected4 = [2, 4]  # -3 + -5 = -8
    result4 = solution.twoSum(nums4, target4)
    assert sorted(result4) == sorted(expected4), f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Zero target
    nums5 = [-1, 0, 1, 2]
    target5 = 0
    expected5 = [0, 2]  # -1 + 1 = 0
    result5 = solution.twoSum(nums5, target5)
    assert sorted(result5) == sorted(expected5), f"Test 5 failed: expected {expected5}, got {result5}"
    
    print("✅ All test cases passed!")


if __name__ == "__main__":
    test_two_sum()