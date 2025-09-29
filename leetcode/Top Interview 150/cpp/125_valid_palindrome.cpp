/*
!Problem: 125. Valid Palindrome
!Difficulty: Easy
!URL: https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



?Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

?Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

?Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


*Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
[constraints here]
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <cctype>
using namespace std;

class Solution
{
public:
    bool isPalindrome(string s)
    {
        int left = 0;
        int right = s.size() - 1;

        while (left <= right)
        {
            while (left < right && !(isalnum(s[left])))
            {
                left += 1;
            }
            while (left < right && !(isalnum(s[right])))
            {
                right -= 1;
            }

            if (tolower(s[left]) != tolower(s[right]))
            {
                return false;
            }
            left += 1;
            right -= 1;
        }

        return true;
    }
};

void test_solution()
{
    Solution solution;

    // Test case 1
    string input1 = "A man, a plan, a canal: Panama";
    bool expected1 = true;
    bool result1 = solution.isPalindrome(input1);
    cout << "Test 1: input = \"" << input1 << "\"" << endl;
    cout << "Expected: " << (expected1 ? "true" : "false") << ", Got: " << (result1 ? "true" : "false") << endl;
    cout << "Pass: " << (result1 == expected1 ? "true" : "false") << endl
         << endl;

    // Test case 2
    string input2 = "race a car";
    bool expected2 = false;
    bool result2 = solution.isPalindrome(input2);
    cout << "Test 2: input = \"" << input2 << "\"" << endl;
    cout << "Expected: " << (expected2 ? "true" : "false") << ", Got: " << (result2 ? "true" : "false") << endl;
    cout << "Pass: " << (result2 == expected2 ? "true" : "false") << endl
         << endl;

    // Test case 3
    string input3 = " ";
    bool expected3 = true;
    bool result3 = solution.isPalindrome(input3);
    cout << "Test 3: input = \"" << input3 << "\"" << endl;
    cout << "Expected: " << (expected3 ? "true" : "false") << ", Got: " << (result3 ? "true" : "false") << endl;
    cout << "Pass: " << (result3 == expected3 ? "true" : "false") << endl
         << endl;

    // Test case 4
    string input4 = "0P";
    bool expected4 = false;
    bool result4 = solution.isPalindrome(input4);
    cout << "Test 4: input = \"" << input4 << "\"" << endl;
    cout << "Expected: " << (expected4 ? "true" : "false") << ", Got: " << (result4 ? "true" : "false") << endl;
    cout << "Pass: " << (result4 == expected4 ? "true" : "false") << endl
         << endl;
}

int main()
{
    test_solution();
    return 0;
}
