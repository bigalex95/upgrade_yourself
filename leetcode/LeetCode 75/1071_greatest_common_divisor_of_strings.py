"""
Problem: 1071. Greatest Common Divisor of Strings
Difficulty: Easy
URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

Description:
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Find the greatest common divisor of two strings.

        A string divides another if it can be formed by concatenating the divisor string.

        Args:
            str1: First input string
            str2: Second input string

        Returns:
            str: The largest string that divides both str1 and str2
        """
        import math

        # Check if concatenation in both orders gives the same result
        # This is the key insight: if str1 + str2 == str2 + str1,
        # then both strings are formed by repeating a common substring
        if str1 + str2 != str2 + str1:
            return ""

        # If they have a common divisor, its length is the GCD of their lengths
        gcd_length = math.gcd(len(str1), len(str2))

        # The GCD string is the first gcd_length characters of either string
        return str1[:gcd_length]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = "ABCABC"  # Replace with actual input
    input2 = "ABC"  # Replace with actual input
    expected = "ABC"  # Replace with expected output
    result = solution.gcdOfStrings(input1, input2)
    print(f"Test 1: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = "ABABAB"  # Replace with actual input
    input2 = "ABAB"  # Replace with actual input
    expected = "AB"  # Replace with expected output
    result = solution.gcdOfStrings(input1, input2)
    print(f"Test 2: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3 - Edge case
    input1 = "LEET"  # Replace with actual input
    input2 = "CODE"  # Replace with actual input
    expected = ""  # Replace with expected output
    result = solution.gcdOfStrings(input1, input2)
    print(f"Test 3: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()
