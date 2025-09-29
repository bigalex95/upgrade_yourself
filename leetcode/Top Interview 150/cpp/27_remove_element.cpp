/*
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
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int k = 0;

        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != val)
            {
                nums[k] = nums[i];
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
    vector<int> nums1 = {3, 2, 2, 3};
    int val1 = 3;
    int expected1 = 2;
    int k1 = solution.removeElement(nums1, val1);
    cout << "Test 1: Expected = " << expected1 << ", Got = " << k1 << endl;
    assert(k1 == expected1);

    // Test case 2
    vector<int> nums2 = {0, 1, 2, 2, 3, 0, 4, 2};
    int val2 = 2;
    int expected2 = 5;
    int k2 = solution.removeElement(nums2, val2);
    cout << "Test 2: Expected = " << expected2 << ", Got = " << k2 << endl;
    assert(k2 == expected2);

    // Test case 3: No elements to remove
    vector<int> nums3 = {1, 2, 3, 4};
    int val3 = 5;
    int expected3 = 4;
    int k3 = solution.removeElement(nums3, val3);
    cout << "Test 3: Expected = " << expected3 << ", Got = " << k3 << endl;
    assert(k3 == expected3);

    // Test case 4: All elements to remove
    vector<int> nums4 = {2, 2, 2};
    int val4 = 2;
    int expected4 = 0;
    int k4 = solution.removeElement(nums4, val4);
    cout << "Test 4: Expected = " << expected4 << ", Got = " << k4 << endl;
    assert(k4 == expected4);

    // Test case 5: Empty array
    vector<int> nums5 = {};
    int val5 = 1;
    int expected5 = 0;
    int k5 = solution.removeElement(nums5, val5);
    cout << "Test 5: Expected = " << expected5 << ", Got = " << k5 << endl;
    assert(k5 == expected5);
}

int main()
{
    test_solution();
    return 0;
}
