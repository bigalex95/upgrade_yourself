/*
!Problem: 15. 3Sum
!Difficulty: Medium
!URL: https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



?Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

?Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

?Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


*Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

class Solution
{
public:
    // [Brief description of what this function does]
    // param1: [description]
    // param2: [description]
    // return: [description of return value]
    int functionName(int param1, int param2)
    {
        // TODO: Implement solution here
        return 0;
    }
};

void test_solution()
{
    Solution solution;

    // Test case 1
    int input1 = 0;   // Replace with actual input
    int input2 = 0;   // Replace with actual input
    int expected = 0; // Replace with expected output

    cout << "Test 1: input1 = " << input1 << ", input2 = " << input2 << endl;
    int result = solution.functionName(input1, input2);
    cout << "Expected: " << expected << ", Got: " << result << endl;
    cout << "Pass: " << (result == expected ? "true" : "false") << endl
         << endl;

    // Add more test cases as needed
}

int main()
{
    test_solution();
    return 0;
}
