/*
!Problem: 392. Is Subsequence
!Difficulty: Easy
!URL: https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



?Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

?Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


*Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
*/

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int s_idx = 0;
        int t_idx = 0;

        while (s_idx < s.size() && t_idx < t.size())
        {
            if (s[s_idx] == t[t_idx])
            {
                s_idx += 1;
            }
            t_idx += 1;
        }

        return s_idx == s.size();
    }
};

void test_solution()
{
    Solution solution;

    // Test case 1
    string s1 = "abc";
    string t1 = "ahbgdc";
    bool expected1 = true;
    bool result1 = solution.isSubsequence(s1, t1);
    cout << "Test 1: s = \"" << s1 << "\", t = \"" << t1 << "\"" << endl;
    cout << "Expected: " << (expected1 ? "true" : "false") << ", Got: " << (result1 ? "true" : "false") << endl;
    cout << "Pass: " << (result1 == expected1 ? "true" : "false") << endl
         << endl;

    // Test case 2
    string s2 = "axc";
    string t2 = "ahbgdc";
    bool expected2 = false;
    bool result2 = solution.isSubsequence(s2, t2);
    cout << "Test 2: s = \"" << s2 << "\", t = \"" << t2 << "\"" << endl;
    cout << "Expected: " << (expected2 ? "true" : "false") << ", Got: " << (result2 ? "true" : "false") << endl;
    cout << "Pass: " << (result2 == expected2 ? "true" : "false") << endl
         << endl;

    // Test case 3: empty s
    string s3 = "";
    string t3 = "ahbgdc";
    bool expected3 = true;
    bool result3 = solution.isSubsequence(s3, t3);
    cout << "Test 3: s = \"" << s3 << "\", t = \"" << t3 << "\"" << endl;
    cout << "Expected: " << (expected3 ? "true" : "false") << ", Got: " << (result3 ? "true" : "false") << endl;
    cout << "Pass: " << (result3 == expected3 ? "true" : "false") << endl
         << endl;

    // Test case 4: empty t
    string s4 = "a";
    string t4 = "";
    bool expected4 = false;
    bool result4 = solution.isSubsequence(s4, t4);
    cout << "Test 4: s = \"" << s4 << "\", t = \"" << t4 << "\"" << endl;
    cout << "Expected: " << (expected4 ? "true" : "false") << ", Got: " << (result4 ? "true" : "false") << endl;
    cout << "Pass: " << (result4 == expected4 ? "true" : "false") << endl
         << endl;

    // Test case 5: both empty
    string s5 = "";
    string t5 = "";
    bool expected5 = true;
    bool result5 = solution.isSubsequence(s5, t5);
    cout << "Test 5: s = \"" << s5 << "\", t = \"" << t5 << "\"" << endl;
    cout << "Expected: " << (expected5 ? "true" : "false") << ", Got: " << (result5 ? "true" : "false") << endl;
    cout << "Pass: " << (result5 == expected5 ? "true" : "false") << endl
         << endl;

    // Test case 6
    string s6 = "acb";
    string t6 = "ahbgdc";
    bool expected6 = false;
    bool result6 = solution.isSubsequence(s6, t6);
    cout << "Test 6: s = \"" << s6 << "\", t = \"" << t6 << "\"" << endl;
    cout << "Expected: " << (expected6 ? "true" : "false") << ", Got: " << (result6 ? "true" : "false") << endl;
    cout << "Pass: " << (result6 == expected6 ? "true" : "false") << endl
         << endl;
}

int main()
{
    test_solution();
    return 0;
}
