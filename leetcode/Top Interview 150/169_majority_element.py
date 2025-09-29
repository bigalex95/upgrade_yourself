"""
!Problem: 169. Majority Element
!Difficulty: Easy
!URL: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


?Example 1:

Input: nums = [3,2,3]
Output: 3

?Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


*Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


*Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     """
    #     Finds the majority element in a list of integers.
    #     The majority element is the element that appears more than ⌊n / 2⌋ times,
    #     where n is the length of the list. Assumes that the input list always contains
    #     a majority element.
    #     Args:
    #         nums (List[int]): A list of integers.
    #     Returns:
    #         int: The majority element in the list.
    #     """

    #     tmp = {}

    #     for num in nums:
    #         if tmp.get(num) is None:
    #             tmp[num] = 1
    #         else:
    #             tmp[num] += 1

    #     majority_element = max(tmp, key=lambda k: tmp[k])

    #     return majority_element

    # !Boyer-Moore Algorithm (Python):
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 3]
    expected1 = 3
    result1 = solution.majorityElement(nums1)
    print(f"Test 1: nums={nums1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    expected2 = 2
    result2 = solution.majorityElement(nums2)
    print(f"Test 2: nums={nums2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}\n")

    # Test case 3
    nums3 = [1]
    expected3 = 1
    result3 = solution.majorityElement(nums3)
    print(f"Test 3: nums={nums3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}\n")


if __name__ == "__main__":
    test_solution()
