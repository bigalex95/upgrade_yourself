/*
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
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int idx = 0;
        int idx1 = 0;
        int idx2 = 0;
        vector<int> tmp_num1(nums1.begin(), nums1.begin() + m);

        while (idx1 < m and idx2 < n)
        {
            if (tmp_num1[idx1] < nums2[idx2])
            {
                nums1[idx] = tmp_num1[idx1];
                idx1 += 1;
            }
            else
            {
                nums1[idx] = nums2[idx2];
                idx2 += 1;
            }
            idx += 1;
        }

        if (idx1 < m)
        {
            std::copy(tmp_num1.begin() + idx1, tmp_num1.end(), nums1.begin() + idx);
        }
        if (idx2 < n)
        {
            std::copy(nums2.begin() + idx2, nums2.end(), nums1.begin() + idx);
        }
    }
};

void test_solution()
{
    Solution solution;

    // Test case 1
    vector<int> nums1 = {1, 2, 3, 0, 0, 0};
    int m = 3;
    vector<int> nums2 = {2, 5, 6};
    int n = 3;
    vector<int> expected = {1, 2, 2, 3, 5, 6};

    cout << "Test 1: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3" << endl;
    solution.merge(nums1, m, nums2, n);
    cout << "Expected: [1,2,2,3,5,6], Got: [";
    for (size_t i = 0; i < nums1.size(); ++i)
    {
        cout << nums1[i];
        if (i != nums1.size() - 1)
            cout << ",";
    }
    cout << "]" << endl;
    cout << "Pass: " << (nums1 == expected ? "true" : "false") << endl
         << endl;

    // Test case 2
    nums1 = {1};
    m = 1;
    nums2 = {};
    n = 0;
    expected = {1};

    cout << "Test 2: nums1 = [1], m = 1, nums2 = [], n = 0" << endl;
    solution.merge(nums1, m, nums2, n);
    cout << "Expected: [1], Got: [";
    for (size_t i = 0; i < nums1.size(); ++i)
    {
        cout << nums1[i];
        if (i != nums1.size() - 1)
            cout << ",";
    }
    cout << "]" << endl;
    cout << "Pass: " << (nums1 == expected ? "true" : "false") << endl
         << endl;

    // Test case 3
    nums1 = {0};
    m = 0;
    nums2 = {1};
    n = 1;
    expected = {1};

    cout << "Test 3: nums1 = [0], m = 0, nums2 = [1], n = 1" << endl;
    solution.merge(nums1, m, nums2, n);
    cout << "Expected: [1], Got: [";
    for (size_t i = 0; i < nums1.size(); ++i)
    {
        cout << nums1[i];
        if (i != nums1.size() - 1)
            cout << ",";
    }
    cout << "]" << endl;
    cout << "Pass: " << (nums1 == expected ? "true" : "false") << endl
         << endl;
}

int main()
{
    test_solution();
    return 0;
}
