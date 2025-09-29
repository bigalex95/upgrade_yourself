/*
!Problem: 167. Two Sum II - Input Array Is Sorted
!Difficulty: Medium
!URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



?Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

?Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

?Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


*Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        vector<int> tmp = {0, 0};
        int left = 0;
        int right = numbers.size() - 1;

        while (left < right)
        {
            if (numbers[left] + numbers[right] == target)
            {
                tmp[0] = left + 1;
                tmp[1] = right + 1;
                return tmp;
            }
            else if (numbers[left] + numbers[right] < target)
            {
                left += 1;
            }
            else
            {
                right -= 1;
            }
        }

        return tmp;
    }
};

void test_solution()
{
    Solution solution;

    // Test case 1
    vector<int> numbers1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> expected1 = {1, 2};
    vector<int> result1 = solution.twoSum(numbers1, target1);
    cout << "Test 1: ";
    cout << "Expected: [" << expected1[0] << "," << expected1[1] << "], Got: [" << result1[0] << "," << result1[1] << "]";
    cout << " Pass: " << (result1 == expected1 ? "true" : "false") << endl;

    // Test case 2
    vector<int> numbers2 = {2, 3, 4};
    int target2 = 6;
    vector<int> expected2 = {1, 3};
    vector<int> result2 = solution.twoSum(numbers2, target2);
    cout << "Test 2: ";
    cout << "Expected: [" << expected2[0] << "," << expected2[1] << "], Got: [" << result2[0] << "," << result2[1] << "]";
    cout << " Pass: " << (result2 == expected2 ? "true" : "false") << endl;

    // Test case 3
    vector<int> numbers3 = {-1, 0};
    int target3 = -1;
    vector<int> expected3 = {1, 2};
    vector<int> result3 = solution.twoSum(numbers3, target3);
    cout << "Test 3: ";
    cout << "Expected: [" << expected3[0] << "," << expected3[1] << "], Got: [" << result3[0] << "," << result3[1] << "]";
    cout << " Pass: " << (result3 == expected3 ? "true" : "false") << endl;
}

int main()
{
    test_solution();
    return 0;
}
