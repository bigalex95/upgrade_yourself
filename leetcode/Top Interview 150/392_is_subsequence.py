"""
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
"""


class Solution:
    # #! My solution v1
    # def isSubsequence(self, s: str, t: str) -> bool:

    #     if len(s) > len(t):
    #         return False

    #     s_idx = 0
    #     t_idx = 0

    #     while s_idx < len(s) and t_idx < len(t):
    #         if t[t_idx:].find(s[s_idx]) >= 0:
    #             t_idx += t[t_idx:].find(s[s_idx]) + 1
    #         else:
    #             return False

    #         s_idx += 1

    #     if s_idx < len(s):
    #         return False

    #     return True

    #! My solution v2
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Check if s is a subsequence of t using string find method.

        APPROACH: Sequential character search with find()
        - For each character in s, find it in the remaining part of t
        - Move search position past the found character
        - Time: O(n*m) worst case, Space: O(1)

        Note: Two-pointer approach would be more efficient O(n+m)

        Args:
            s: String to check if it's a subsequence
            t: String to check subsequence against

        Returns:
            bool: True if s is subsequence of t, False otherwise
        """
        char_index = 0
        for char in s:
            idx = t[char_index:].find(char)
            if idx >= 0:
                char_index += idx + 1  # Move past found character
            else:
                return False

        return True

    # #! Solution from leetcode
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     sp = tp = 0

    #     while sp < len(s) and tp < len(t):
    #         if s[sp] == t[tp]:
    #             sp += 1
    #         tp += 1

    #     return sp == len(s)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    s1 = "abc"
    t1 = "ahbgdc"
    expected1 = True
    result1 = solution.isSubsequence(s1, t1)
    print(f"Test 1: s='{s1}', t='{t1}'")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test case 2
    s2 = "acb"
    t2 = "ahbgdc"
    expected2 = False
    result2 = solution.isSubsequence(s2, t2)
    print(f"Test 2: s='{s2}', t='{t2}'")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}\n")

    # Test case 3: empty s
    s3 = ""
    t3 = "ahbgdc"
    expected3 = True
    result3 = solution.isSubsequence(s3, t3)
    print(f"Test 3: s='{s3}', t='{t3}'")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}\n")

    # Test case 4: empty t
    s4 = "a"
    t4 = ""
    expected4 = False
    result4 = solution.isSubsequence(s4, t4)
    print(f"Test 4: s='{s4}', t='{t4}'")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4}\n")

    # Test case 5: both empty
    s5 = ""
    t5 = ""
    expected5 = True
    result5 = solution.isSubsequence(s5, t5)
    print(f"Test 5: s='{s5}', t='{t5}'")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {result5 == expected5}\n")


if __name__ == "__main__":
    test_solution()
