"""
LeetCode Problem: 1768. Merge Strings Alternately
Difficulty: Easy
URL: https://leetcode.com/problems/merge-strings-alternately/

Description:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d


Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately.

        Args:
            word1: First string
            word2: Second string

        Returns:
            str: Merged string with characters alternating between word1 and word2
        """
        result = ""
        min_len = min(len(word1), len(word2))

        # Alternate characters from both strings
        for i in range(min_len):
            result += word1[i] + word2[i]

        # Add remaining characters from the longer string
        if len(word1) > len(word2):
            result += word1[min_len:]
        else:
            result += word2[min_len:]

        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    word1, word2 = "abc", "pqr"
    expected = "apbqcr"
    result = solution.mergeAlternately(word1, word2)
    print(f"Test 1: word1='{word1}', word2='{word2}'")
    print(f"Expected: '{expected}', Got: '{result}'")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    word1, word2 = "ab", "pqrs"
    expected = "apbqrs"
    result = solution.mergeAlternately(word1, word2)
    print(f"Test 2: word1='{word1}', word2='{word2}'")
    print(f"Expected: '{expected}', Got: '{result}'")
    print(f"Pass: {result == expected}\n")

    # Test case 3
    word1, word2 = "abcd", "pq"
    expected = "apbqcd"
    result = solution.mergeAlternately(word1, word2)
    print(f"Test 3: word1='{word1}', word2='{word2}'")
    print(f"Expected: '{expected}', Got: '{result}'")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()
