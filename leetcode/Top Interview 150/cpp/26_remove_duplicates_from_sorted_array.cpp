/*
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
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <map>
using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        map<int, int> tmp;

        for (int num : nums)
        {
            tmp[num] = 1;
        }

        int i = 0;
        for (const auto &[key, _] : tmp)
        {
            nums[i++] = key;
        }

        return tmp.size();
    }
};

void test_solution()
{
    Solution solution;

    // Test case 1
    vector<int> nums1 = {1, 1, 2};
    int expected1 = 2;
    int result1 = solution.removeDuplicates(nums1);
    assert(result1 == expected1);
    assert(nums1[0] == 1 && nums1[1] == 2);

    // Test case 2
    vector<int> nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int expected2 = 5;
    int result2 = solution.removeDuplicates(nums2);
    assert(result2 == expected2);
    assert(nums2[0] == 0 && nums2[1] == 1 && nums2[2] == 2 && nums2[3] == 3 && nums2[4] == 4);

    // Test case 3: single element
    vector<int> nums3 = {5};
    int expected3 = 1;
    int result3 = solution.removeDuplicates(nums3);
    assert(result3 == expected3);
    assert(nums3[0] == 5);

    // Test case 4: all duplicates
    vector<int> nums4 = {2, 2, 2, 2};
    int expected4 = 1;
    int result4 = solution.removeDuplicates(nums4);
    assert(result4 == expected4);
    assert(nums4[0] == 2);

    // Test case 5: no duplicates
    vector<int> nums5 = {1, 2, 3, 4, 5};
    int expected5 = 5;
    int result5 = solution.removeDuplicates(nums5);
    assert(result5 == expected5);
    assert(nums5[0] == 1 && nums5[1] == 2 && nums5[2] == 3 && nums5[3] == 4 && nums5[4] == 5);

    cout << "All test cases passed!" << endl;
}

int main()
{
    test_solution();
    return 0;
}
