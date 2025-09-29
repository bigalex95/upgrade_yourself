"""
!Problem: 167. Two Sum II - Input Array Is Sorted
!Difficulty: Medium
!URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space. O(1)



?Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

?Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

?Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


*Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers in a sorted list that add up to a specific target and returns their 1-based indices.
        Args:
            numbers (List[int]): A list of integers sorted in non-decreasing order.
            target (int): The target sum to find.
        Returns:
            List[int]: A list containing the 1-based indices of the two numbers whose sum equals the target.
                       Returns an empty list if no such pair exists.
        Example:
            >>> twoSum([2, 7, 11, 15], 9)
            [1, 2]
        """

        result = []
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    numbers = [2, 7, 11, 15]
    target = 9
    expected = [1, 2]
    result = solution.twoSum(numbers, target)
    print(f"Test 1: numbers={numbers}, target={target}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    numbers = [2, 3, 4]
    target = 6
    expected = [1, 3]
    result = solution.twoSum(numbers, target)
    print(f"Test 2: numbers={numbers}, target={target}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3
    numbers = [-1, 0]
    target = -1
    expected = [1, 2]
    result = solution.twoSum(numbers, target)
    print(f"Test 3: numbers={numbers}, target={target}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()
