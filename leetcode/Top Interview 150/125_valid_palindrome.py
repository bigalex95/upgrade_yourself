"""
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
"""

import re


class Solution:
    #! My solution v1
    # def isPalindrome(self, s: str) -> bool:
    #     if len(s) == 0:
    #         return True

    #     left = 0
    #     right = len(s) - 1
    #     s = s.lower()

    #     def valid_char(c: str):
    #         return (
    #             (ord(c) >= 48 and ord(c) <= 57)
    #             or (ord(c) >= 65 and ord(c) <= 90)
    #             or (ord(c) >= 97 and ord(c) <= 122)
    #         )

    #     while left < right:
    #         if valid_char(s[left]) and valid_char(s[right]):
    #             if s[left] == s[right]:
    #                 left += 1
    #                 right -= 1
    #             else:
    #                 return False
    #         elif not valid_char(s[left]):
    #             left += 1
    #         else:
    #             right -= 1

    #     return True

    #! Solution with regular expression
    # def isPalindrome(self, s: str) -> bool:
    #     # Remove non-alphanumeric characters and convert to lowercase

    #     cleaned = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

    #     return cleaned == cleaned[::-1]

    #! My solution v2
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if the given string is a palindrome, considering only alphanumeric characters and ignoring cases.
        Args:
            s (str): The input string to check.
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        The function ignores non-alphanumeric characters and treats uppercase and lowercase letters as equal.
        """
        l, r = 0, len(s) - 1
        while l <= r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    # Test case 1
    s1 = "A man, a plan, a canal: Panama"
    expected1 = True
    result1 = solution.isPalindrome(s1)
    print(f"Test 1: input={s1!r}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test case 2
    s2 = "race a car"
    expected2 = False
    result2 = solution.isPalindrome(s2)
    print(f"Test 2: input={s2!r}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}\n")

    # Test case 3
    s3 = " "
    expected3 = True
    result3 = solution.isPalindrome(s3)
    print(f"Test 3: input={s3!r}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}\n")

    # Test case 4
    s4 = "0P"
    expected4 = False
    result4 = solution.isPalindrome(s4)
    print(f"Test 4: input={s4!r}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4}\n")

    # Test case 5
    s5 = "a."
    expected5 = True
    result5 = solution.isPalindrome(s5)
    print(f"Test 5: input={s5!r}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {result5 == expected5}\n")


if __name__ == "__main__":
    test_solution()
