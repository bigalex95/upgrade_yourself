/*
!Problem: 169. Majority Element
!Difficulty: Easy
!URL: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


?Example 1:

Input: nums = [3,2,3]
Output: 3

?Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


*Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


*Follow-up: Could you solve the problem in linear time and in O(1) space?
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int count = 0;
        int candidate = 0;

        for (int num : nums)
        {
            if (count == 0)
            {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
};

void test_solution()
{
    Solution solution;
    // Test case 1
    vector<int> nums1 = {3, 2, 3};
    int expected1 = 3;
    int result1 = solution.majorityElement(nums1);
    cout << "Test 1: nums = {3, 2, 3}" << endl;
    cout << "Expected: " << expected1 << ", Got: " << result1 << endl;
    assert(result1 == expected1);

    // Test case 2
    vector<int> nums2 = {2, 2, 1, 1, 1, 2, 2};
    int expected2 = 2;
    int result2 = solution.majorityElement(nums2);
    cout << "Test 2: nums = {2, 2, 1, 1, 1, 2, 2}" << endl;
    cout << "Expected: " << expected2 << ", Got: " << result2 << endl;
    assert(result2 == expected2);

    // Test case 3: single element
    vector<int> nums3 = {1};
    int expected3 = 1;
    int result3 = solution.majorityElement(nums3);
    cout << "Test 3: nums = {1}" << endl;
    cout << "Expected: " << expected3 << ", Got: " << result3 << endl;
    assert(result3 == expected3);

    // Test case 4: all elements are the same
    vector<int> nums4 = {5, 5, 5, 5, 5};
    int expected4 = 5;
    int result4 = solution.majorityElement(nums4);
    cout << "Test 4: nums = {5, 5, 5, 5, 5}" << endl;
    cout << "Expected: " << expected4 << ", Got: " << result4 << endl;
    assert(result4 == expected4);

    cout << "All test cases passed!" << endl;
}

int main()
{
    test_solution();
    return 0;
}
