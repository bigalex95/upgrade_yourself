"""
!Problem: 15. 3Sum
!Difficulty: Medium
!URL: https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



?Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

?Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

?Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


*Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = None  # Replace with actual input
    input2 = None  # Replace with actual input
    expected = None  # Replace with expected output
    print(f"Test 1: input1={input1}, input2={input2}")
    result = solution.functionName(input1, input2)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()
