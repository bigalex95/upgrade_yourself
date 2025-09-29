"""
!Problem: 11. Container With Most Water
!Difficulty: Medium
!URL: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.




?Example 1:


9 |
8 |    █              █
7 |    ██████████████████████
6 |    █  █  *  *  *  █  *  █
5 |    █  █  *  █  *  █  *  █
4 |    █  █  *  █  █  █  *  █
3 |    █  █  *  █  █  █  █  █
2 |    █  █  █  █  █  █  █  █
1 | █  █  █  █  █  █  █  █  █
0 +---------------------------->
    0  1  2  3  4  5  6  7  8

Legend:
█ - bar height
Blue area - trapped water (indicated by horizontal line above min(left_max, right_max))
* - water


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

?Example 2:

Input: height = [1,1]
Output: 1


*Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from typing import List


class Solution:
    #! My solution v2
    def maxArea(self, height: List[int]) -> int:
        """
        Find maximum water area using two-pointer technique.

        APPROACH: Two-pointer greedy algorithm
        - Start with widest possible container (left=0, right=n-1)
        - Always move the pointer with smaller height inward
        - Keep track of maximum area found so far
        - Time: O(n), Space: O(1)

        Key insight: Moving the taller line inward can never give a better result
        because the height is limited by the shorter line and width decreases.

        Args:
            height: List of integers representing line heights

        Returns:
            int: Maximum water area that can be contained
        """

        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            water_container = (right - left) * min(height[left], height[right])
            if water_container > max_water:
                max_water = water_container

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected1 = 49
    result1 = solution.maxArea(height1)
    print(f"Test 1: input={height1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test case 2
    height2 = [1, 1]
    expected2 = 1
    result2 = solution.maxArea(height2)
    print(f"Test 2: input={height2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}\n")

    # Test case 3
    height3 = [4, 3, 2, 1, 4]
    expected3 = 16
    result3 = solution.maxArea(height3)
    print(f"Test 3: input={height3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}\n")

    # Test case 4
    height4 = [1, 2, 1]
    expected4 = 2
    result4 = solution.maxArea(height4)
    print(f"Test 4: input={height4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4}\n")


if __name__ == "__main__":
    test_solution()
