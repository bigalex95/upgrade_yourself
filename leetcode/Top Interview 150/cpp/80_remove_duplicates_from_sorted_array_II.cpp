/*
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
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int k = 0;
        for (int num : nums)
        {
            if (k < 2 || num != nums[k - 2])
            {
                nums[k] = num;
                k += 1;
            }
        }
        return k;
    }
};

void test_solution()
{
    Solution solution;

    // Test case 1
    vector<int> nums1 = {1, 1, 1, 2, 2, 3};
    int expected1 = 5;
    int k1 = solution.removeDuplicates(nums1);
    assert(k1 == expected1);
    assert((vector<int>(nums1.begin(), nums1.begin() + k1) == vector<int>{1, 1, 2, 2, 3}));

    // Test case 2
    vector<int> nums2 = {0, 0, 1, 1, 1, 1, 2, 3, 3};
    int expected2 = 7;
    int k2 = solution.removeDuplicates(nums2);
    assert(k2 == expected2);
    assert((vector<int>(nums2.begin(), nums2.begin() + k2) == vector<int>{0, 0, 1, 1, 2, 3, 3}));

    // Test case 3: No duplicates
    vector<int> nums3 = {1, 2, 3, 4};
    int expected3 = 4;
    int k3 = solution.removeDuplicates(nums3);
    assert(k3 == expected3);
    assert((vector<int>(nums3.begin(), nums3.begin() + k3) == vector<int>{1, 2, 3, 4}));

    // Test case 4: All elements are the same
    vector<int> nums4 = {5, 5, 5, 5, 5};
    int expected4 = 2;
    int k4 = solution.removeDuplicates(nums4);
    assert(k4 == expected4);
    assert((vector<int>(nums4.begin(), nums4.begin() + k4) == vector<int>{5, 5}));

    // Test case 5: Single element
    vector<int> nums5 = {7};
    int expected5 = 1;
    int k5 = solution.removeDuplicates(nums5);
    assert(k5 == expected5);
    assert((vector<int>(nums5.begin(), nums5.begin() + k5) == vector<int>{7}));

    cout << "All test cases passed!" << endl;
}

int main()
{
    test_solution();
    return 0;
}
