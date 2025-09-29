"""
!Problem: 80. Remove Duplicates from Sorted Array II
!Difficulty: Medium
!URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


?Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

?Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


*Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place such that each element appears at most twice.
        Args:
            nums (List[int]): The input sorted list of integers.
        Returns:
            int: The length of the modified list after removing extra duplicates.
        The function modifies the input list in-place to ensure that each unique element appears at most twice.
        The relative order of the elements is maintained.
        """

        if nums is None:
            return 0

        if len(nums) == 1:
            return 1

        k = 1
        two_num = False

        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                nums[k] = nums[idx]
                k += 1
                two_num = False
            elif nums[idx] == nums[idx - 1] and two_num == False:
                nums[k] = nums[idx]
                k += 1
                two_num = True

        return k


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    expected1 = [1, 1, 2, 2, 3]
    k1 = solution.removeDuplicates(nums1)
    print(f"Test 1:")
    print(f"  Input:    { [1, 1, 1, 2, 2, 3] }")
    print(f"  Output:   {nums1[:k1]}, k={k1}")
    print(f"  Expected: {expected1}")
    print(f"  Pass:     {nums1[:k1] == expected1 and k1 == len(expected1)}\n")

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected2 = [0, 0, 1, 1, 2, 3, 3]
    k2 = solution.removeDuplicates(nums2)
    print(f"Test 2:")
    print(f"  Input:    { [0, 0, 1, 1, 1, 1, 2, 3, 3] }")
    print(f"  Output:   {nums2[:k2]}, k={k2}")
    print(f"  Expected: {expected2}")
    print(f"  Pass:     {nums2[:k2] == expected2 and k2 == len(expected2)}\n")

    # Test case 3: Single element
    nums3 = [5]
    expected3 = [5]
    k3 = solution.removeDuplicates(nums3)
    print(f"Test 3:")
    print(f"  Input:    { [5] }")
    print(f"  Output:   {nums3[:k3]}, k={k3}")
    print(f"  Expected: {expected3}")
    print(f"  Pass:     {nums3[:k3] == expected3 and k3 == len(expected3)}\n")

    # Test case 4: All elements are the same
    nums4 = [2, 2, 2, 2, 2]
    expected4 = [2, 2]
    k4 = solution.removeDuplicates(nums4)
    print(f"Test 4:")
    print(f"  Input:    { [2, 2, 2, 2, 2] }")
    print(f"  Output:   {nums4[:k4]}, k={k4}")
    print(f"  Expected: {expected4}")
    print(f"  Pass:     {nums4[:k4] == expected4 and k4 == len(expected4)}\n")

    # Test case 5: No duplicates
    nums5 = [1, 2, 3, 4, 5]
    expected5 = [1, 2, 3, 4, 5]
    k5 = solution.removeDuplicates(nums5)
    print(f"Test 5:")
    print(f"  Input:    { [1, 2, 3, 4, 5] }")
    print(f"  Output:   {nums5[:k5]}, k={k5}")
    print(f"  Expected: {expected5}")
    print(f"  Pass:     {nums5[:k5] == expected5 and k5 == len(expected5)}\n")


if __name__ == "__main__":
    test_solution()
