/*
!Problem: 11. Container With Most Water
!Difficulty: Medium
!URL: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.




?Example 1:


9 |
8 |    █              █
7 |    ██████████████████████
6 |    █  █  *  *  *  █  *  █
5 |    █  █  *  █  *  █  *  █
4 |    █  █  *  █  █  █  *  █
3 |    █  █  *  █  █  █  █  █
2 |    █  █  █  █  █  █  █  █
1 | █  █  █  █  █  █  █  █  █
0 +---------------------------->
    0  1  2  3  4  5  6  7  8

Legend:
█ - bar height
Blue area - trapped water (indicated by horizontal line above min(left_max, right_max))
* - water


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

?Example 2:

Input: height = [1,1]
Output: 1


*Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int left = 0;
        int right = height.size() - 1;
        int max_water = 0;

        while (left < right)
        {
            max_water = max(max_water, (right - left) * min(height[left], height[right]));

            if (height[left] < height[right])
            {
                left += 1;
            }
            else
            {
                right -= 1;
            }
        }

        return max_water;
    }
};

void test_solution()
{
    Solution solution;
    // Test case 1
    vector<int> height1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int expected1 = 49;
    int result1 = solution.maxArea(height1);
    cout << "Test 1: Expected: " << expected1 << ", Got: " << result1 << endl;
    assert(result1 == expected1);

    // Test case 2
    vector<int> height2 = {1, 1};
    int expected2 = 1;
    int result2 = solution.maxArea(height2);
    cout << "Test 2: Expected: " << expected2 << ", Got: " << result2 << endl;
    assert(result2 == expected2);

    // Test case 3
    vector<int> height3 = {4, 3, 2, 1, 4};
    int expected3 = 16;
    int result3 = solution.maxArea(height3);
    cout << "Test 3: Expected: " << expected3 << ", Got: " << result3 << endl;
    assert(result3 == expected3);

    // Test case 4
    vector<int> height4 = {1, 2, 1};
    int expected4 = 2;
    int result4 = solution.maxArea(height4);
    cout << "Test 4: Expected: " << expected4 << ", Got: " << result4 << endl;
    assert(result4 == expected4);
}

int main()
{
    test_solution();
    return 0;
}
