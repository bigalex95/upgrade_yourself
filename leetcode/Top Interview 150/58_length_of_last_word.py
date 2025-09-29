"""
!Problem: 58. Length of Last Word
!Difficulty: Easy
!URL: https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

*Description:

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space chacters only.



?Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

?Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

?Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


*Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        # Count the length of the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    s1 = "Hello World"
    expected1 = 5
    result1 = solution.lengthOfLastWord(s1)
    print(f"Test 1: input={s1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test case 2
    s2 = "   fly me   to   the moon  "
    expected2 = 4
    result2 = solution.lengthOfLastWord(s2)
    print(f"Test 2: input={s2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}\n")

    # Test case 3
    s3 = "luffy is still joyboy"
    expected3 = 6
    result3 = solution.lengthOfLastWord(s3)
    print(f"Test 3: input={s3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}\n")


if __name__ == "__main__":
    test_solution()
