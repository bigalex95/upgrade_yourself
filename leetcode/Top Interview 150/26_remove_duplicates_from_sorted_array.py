"""
!Problem: 26. Remove Duplicates from Sorted Array
!Difficulty: Easy
!URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
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

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

?Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

*Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted list of integers in-place and returns the number of unique elements.
        Args:
            nums (List[int]): A list of sorted integers.
        Returns:
            int: The number of unique elements remaining after duplicates are removed.
        Note:
            The function modifies the input list `nums` in-place such that the first `k` elements of `nums`
            contain the unique elements, where `k` is the returned value.
        """

        tmp = {}

        for num in nums:
            tmp[num] = 1

        nums[: len(tmp)] = tmp.keys()

        return len(tmp)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 2]
    expected1 = 2
    result1 = solution.removeDuplicates(nums1)
    print(f"Test 1: nums={nums1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1 and nums1[:result1] == [1, 2]}\n")

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected2 = 5
    result2 = solution.removeDuplicates(nums2)
    print(f"Test 2: nums={nums2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2 and nums2[:result2] == [0, 1, 2, 3, 4]}\n")

    # Test case 3
    nums3 = [1]
    expected3 = 1
    result3 = solution.removeDuplicates(nums3)
    print(f"Test 3: nums={nums3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3 and nums3[:result3] == [1]}\n")

    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    expected4 = 5
    result4 = solution.removeDuplicates(nums4)
    print(f"Test 4: nums={nums4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4 and nums4[:result4] == [1, 2, 3, 4, 5]}\n")

    # Test case 5
    nums5 = [2, 2, 2, 2, 2]
    expected5 = 1
    result5 = solution.removeDuplicates(nums5)
    print(f"Test 5: nums={nums5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {result5 == expected5 and nums5[:result5] == [2]}\n")


if __name__ == "__main__":
    test_solution()
