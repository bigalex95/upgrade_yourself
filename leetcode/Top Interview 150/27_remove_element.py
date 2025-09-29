"""
!Problem: 27. Remove Element
!Difficulty: Easy
!URL: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


?Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

?Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


*Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all instances of `val` from the list `nums` in-place and returns the new length.
        Args:
            nums (List[int]): The list of integers to process.
            val (int): The value to remove from the list.
        Returns:
            int: The number of elements remaining after removal.
        Note:
            The first `k` elements of `nums` will contain the elements that are not equal to `val`.
            The order of elements can be changed. Elements beyond the returned length are not guaranteed to be in any particular order.
        """

        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    expected_k1 = 2
    expected_nums1 = [2, 2]
    k1 = solution.removeElement(nums1, val1)
    print(f"Test 1: nums={nums1}, val={val1}")
    print(f"Expected k: {expected_k1}, Got: {k1}")
    print(
        f"Pass: {k1 == expected_k1 and sorted(nums1[:k1]) == sorted(expected_nums1)}\n"
    )

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    expected_k2 = 5
    expected_nums2 = [0, 1, 4, 0, 3]
    k2 = solution.removeElement(nums2, val2)
    print(f"Test 2: nums={nums2}, val={val2}")
    print(f"Expected k: {expected_k2}, Got: {k2}")
    print(
        f"Pass: {k2 == expected_k2 and sorted(nums2[:k2]) == sorted(expected_nums2)}\n"
    )

    # Test case 3: No elements to remove
    nums3 = [1, 2, 3, 4]
    val3 = 5
    expected_k3 = 4
    expected_nums3 = [1, 2, 3, 4]
    k3 = solution.removeElement(nums3, val3)
    print(f"Test 3: nums={nums3}, val={val3}")
    print(f"Expected k: {expected_k3}, Got: {k3}")
    print(
        f"Pass: {k3 == expected_k3 and sorted(nums3[:k3]) == sorted(expected_nums3)}\n"
    )

    # Test case 4: All elements to remove
    nums4 = [2, 2, 2]
    val4 = 2
    expected_k4 = 0
    expected_nums4 = []
    k4 = solution.removeElement(nums4, val4)
    print(f"Test 4: nums={nums4}, val={val4}")
    print(f"Expected k: {expected_k4}, Got: {k4}")
    print(f"Pass: {k4 == expected_k4 and nums4[:k4] == expected_nums4}\n")

    # Test case 5: Empty array
    nums5 = []
    val5 = 1
    expected_k5 = 0
    expected_nums5 = []
    k5 = solution.removeElement(nums5, val5)
    print(f"Test 5: nums={nums5}, val={val5}")
    print(f"Expected k: {expected_k5}, Got: {k5}")
    print(f"Pass: {k5 == expected_k5 and nums5[:k5] == expected_nums5}\n")


if __name__ == "__main__":
    test_solution()
