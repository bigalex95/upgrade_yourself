/*
Two Sum
LeetCode #1: https://leetcode.com/problems/two-sum/
NeetCode: https://neetcode.io/problems/two-integer-sum

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Time Complexity: O(n)
Space Complexity: O(n)
*/

#include <vector>
#include <unordered_map>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

class Solution
{
public:
    /**
     * Find two numbers in the array that add up to the target.
     *
     * @param nums: vector of integers
     * @param target: target sum
     * @return vector of two indices whose values sum to target
     */
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> numMap;

        for (size_t i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];

            if (numMap.find(complement) != numMap.end())
            {
                return {numMap[complement], static_cast<int>(i)};
            }

            numMap[nums[i]] = static_cast<int>(i);
        }

        return {}; // No solution found
    }
};

// Helper function to check if result is valid
bool isValidResult(vector<int> &nums, int target, vector<int> &result)
{
    if (result.size() != 2)
        return false;
    if (result[0] == result[1])
        return false;
    if (result[0] < 0 || static_cast<size_t>(result[0]) >= nums.size())
        return false;
    if (result[1] < 0 || static_cast<size_t>(result[1]) >= nums.size())
        return false;
    return nums[result[0]] + nums[result[1]] == target;
}

// Test function
void runTests()
{
    Solution solution;

    // Test case 1
    {
        vector<int> nums = {2, 7, 11, 15};
        int target = 9;
        vector<int> result = solution.twoSum(nums, target);
        assert(isValidResult(nums, target, result));

        vector<int> expected = {0, 1};
        sort(result.begin(), result.end());
        sort(expected.begin(), expected.end());
        assert(result == expected);
        cout << "✅ Test 1 passed" << endl;
    }

    // Test case 2
    {
        vector<int> nums = {3, 2, 4};
        int target = 6;
        vector<int> result = solution.twoSum(nums, target);
        assert(isValidResult(nums, target, result));

        vector<int> expected = {1, 2};
        sort(result.begin(), result.end());
        sort(expected.begin(), expected.end());
        assert(result == expected);
        cout << "✅ Test 2 passed" << endl;
    }

    // Test case 3
    {
        vector<int> nums = {3, 3};
        int target = 6;
        vector<int> result = solution.twoSum(nums, target);
        assert(isValidResult(nums, target, result));

        vector<int> expected = {0, 1};
        sort(result.begin(), result.end());
        sort(expected.begin(), expected.end());
        assert(result == expected);
        cout << "✅ Test 3 passed" << endl;
    }

    // Test case 4: Negative numbers
    {
        vector<int> nums = {-1, -2, -3, -4, -5};
        int target = -8;
        vector<int> result = solution.twoSum(nums, target);
        assert(isValidResult(nums, target, result));

        vector<int> expected = {2, 4}; // -3 + -5 = -8
        sort(result.begin(), result.end());
        sort(expected.begin(), expected.end());
        assert(result == expected);
        cout << "✅ Test 4 passed" << endl;
    }

    // Test case 5: Zero target
    {
        vector<int> nums = {-1, 0, 1, 2};
        int target = 0;
        vector<int> result = solution.twoSum(nums, target);
        assert(isValidResult(nums, target, result));

        vector<int> expected = {0, 2}; // -1 + 1 = 0
        sort(result.begin(), result.end());
        sort(expected.begin(), expected.end());
        assert(result == expected);
        cout << "✅ Test 5 passed" << endl;
    }

    cout << "🎉 All tests passed!" << endl;
}

int main()
{
    runTests();
    return 0;
}
