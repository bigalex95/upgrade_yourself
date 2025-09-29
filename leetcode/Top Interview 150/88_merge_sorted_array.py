"""
!Problem: 88. Merge Sorted Array
!Difficulty: Easy
!URL: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

*Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


?Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

?Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

?Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


*Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


*Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted integer arrays nums1 and nums2 into nums1 as one sorted array in-place.
        Args:
            nums1 (List[int]): The first sorted array with a size of m + n, where the first m elements denote the elements to merge, and the last n elements are set to 0 and should be ignored.
            m (int): The number of initialized elements in nums1.
            nums2 (List[int]): The second sorted array with n elements.
            n (int): The number of elements in nums2.
        Returns:
            None: Modifies nums1 in-place to contain the merged sorted array.
        """
        # TODO:Do not return anything, modify nums1 in-place instead.

        idx = 0
        idx1 = 0
        idx2 = 0
        tmp_num1 = nums1[:m]

        while idx1 < m and idx2 < n:
            if tmp_num1[idx1] < nums2[idx2]:
                nums1[idx] = tmp_num1[idx1]
                idx1 += 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 += 1
            idx += 1
        if idx1 < m:
            nums1[idx:] = tmp_num1[idx1:]
        if idx2 < n:
            nums1[idx:] = nums2[idx2:]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]  # Replace with actual input
    m = 3
    nums2 = [2, 5, 6]  # Replace with actual input
    n = 3
    expected = [1, 2, 2, 3, 5, 6]  # Replace with expected output
    print(f"Test 1: input1={nums1}, input2={nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"Expected: {expected}, Got: {nums1}")
    print(f"Pass: {nums1 == expected}\n")

    # Test case 2
    nums1 = [1]  # Replace with actual input
    m = 1
    nums2 = []  # Replace with actual input
    n = 0
    expected = [1]  # Replace with expected output
    print(f"Test 2: input1={nums1}, input2={nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"Expected: {expected}, Got: {nums1}")
    print(f"Pass: {nums1 == expected}\n")

    # Test case 3
    nums1 = [0]  # Replace with actual input
    m = 0
    nums2 = [1]  # Replace with actual input
    n = 1
    expected = [1]  # Replace with expected output
    print(f"Test 3: input1={nums1}, input2={nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"Expected: {expected}, Got: {nums1}")
    print(f"Pass: {nums1 == expected}\n")


if __name__ == "__main__":
    test_solution()
