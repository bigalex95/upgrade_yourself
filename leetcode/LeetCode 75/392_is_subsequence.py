"""
Problem: 392. Is Subsequence
Difficulty: Easy
URL: https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

Description:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence.
In this scenario, how would you change your code?
"""


class Solution:
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


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = "abc"
    input2 = "ahbgdc"
    expected = True
    result = solution.isSubsequence(input1, input2)
    print(f"Test 1: s='{input1}', t='{input2}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = "axc"
    input2 = "ahbgdc"
    expected = False
    result = solution.isSubsequence(input1, input2)
    print(f"Test 2: s='{input1}', t='{input2}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3 - Empty s
    input1 = ""
    input2 = "ahbgdc"
    expected = True  # Empty string is subsequence of any string
    result = solution.isSubsequence(input1, input2)
    print(f"Test 3: s='{input1}', t='{input2}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 4 - Both empty
    input1 = ""
    input2 = ""
    expected = True
    result = solution.isSubsequence(input1, input2)
    print(f"Test 4: s='{input1}', t='{input2}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 5 - Single character match
    input1 = "b"
    input2 = "abc"
    expected = True
    result = solution.isSubsequence(input1, input2)
    print(f"Test 5: s='{input1}', t='{input2}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 6 - Repeated characters
    input1 = "aa"
    input2 = "aab"
    expected = True
    result = solution.isSubsequence(input1, input2)
    print(f"Test 6: s='{input1}', t='{input2}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
SOLUTION ANALYSIS:

YOUR APPROACH: String find() method
✅ CORRECT: You fixed the original bug (char_index += idx + 1)
✅ WORKING: Passes all test cases
⚠️  PERFORMANCE: Not optimal for the follow-up scenario

ALGORITHM EXPLANATION:

Your approach uses the string find() method:
1. For each character in s, find it in the remaining part of t
2. Move the search position past the found character
3. If any character is not found, return False
4. If all characters are found in order, return True

EXAMPLE WALKTHROUGH: s="abc", t="ahbgdc"

Step 1: Find 'a' in t[0:] = "ahbgdc"
  - find('a') returns 0
  - char_index = 0 + 0 + 1 = 1

Step 2: Find 'b' in t[1:] = "hbgdc"  
  - find('b') returns 1
  - char_index = 1 + 1 + 1 = 3

Step 3: Find 'c' in t[3:] = "gdc"
  - find('c') returns 2  
  - char_index = 3 + 2 + 1 = 6

All characters found → return True

ALTERNATIVE APPROACHES:

# Approach 1: Your Current Implementation (String find)
# Time: O(n*m) worst case, Space: O(1)
def isSubsequence_v1(self, s: str, t: str) -> bool:
    char_index = 0
    for char in s:
        idx = t[char_index:].find(char)
        if idx >= 0:
            char_index += idx + 1
        else:
            return False
    return True

# Approach 2: Two-Pointer (OPTIMAL)
# Time: O(n+m), Space: O(1)  
def isSubsequence_v2(self, s: str, t: str) -> bool:
    i, j = 0, 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == len(s)

# Approach 3: Recursive
# Time: O(n+m), Space: O(min(n,m)) due to recursion stack
def isSubsequence_v3(self, s: str, t: str) -> bool:
    def helper(i, j):
        if i == len(s):
            return True
        if j == len(t):
            return False
        
        if s[i] == t[j]:
            return helper(i + 1, j + 1)
        else:
            return helper(i, j + 1)
    
    return helper(0, 0)

# Approach 4: Dynamic Programming  
# Time: O(n*m), Space: O(n*m)
def isSubsequence_v4(self, s: str, t: str) -> bool:
    m, n = len(s), len(t)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty s is subsequence of any t
    for j in range(n + 1):
        dp[0][j] = True
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    
    return dp[m][n]

# Approach 5: Built-in Iterator (Python-specific)
# Time: O(n+m), Space: O(1)
def isSubsequence_v5(self, s: str, t: str) -> bool:
    it = iter(t)
    return all(char in it for char in s)

PERFORMANCE COMPARISON:

Approach 1 (Your find-based):
  ⚠️  O(n*m) time in worst case
  ✅ O(1) space
  ✅ Intuitive and readable
  ❌ Not optimal for follow-up

Approach 2 (Two-pointer):
  ✅ O(n+m) time - optimal
  ✅ O(1) space  
  ✅ Most efficient
  ✅ Best for follow-up scenario

Approach 3 (Recursive):
  ✅ O(n+m) time
  ❌ O(min(n,m)) space
  ✅ Easy to understand
  ❌ Can cause stack overflow

Approach 4 (Dynamic Programming):
  ❌ O(n*m) time
  ❌ O(n*m) space
  ✅ Solves related problems
  ❌ Overkill for this problem

Approach 5 (Iterator):
  ✅ O(n+m) time
  ✅ O(1) space
  ✅ Very Pythonic
  ✅ Concise one-liner

FOLLOW-UP QUESTION ANALYSIS:

"Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9"

For this scenario, you'd want to PREPROCESS t:

# Follow-up Solution: Preprocess t with character positions
# Preprocessing: O(n), Each query: O(m * log(positions))
class Solution:
    def __init__(self):
        self.char_positions = {}
    
    def preprocess(self, t: str):
        from collections import defaultdict
        import bisect
        
        self.char_positions = defaultdict(list)
        for i, char in enumerate(t):
            self.char_positions[char].append(i)
    
    def isSubsequence(self, s: str) -> bool:
        import bisect
        
        current_pos = -1
        for char in s:
            if char not in self.char_positions:
                return False
            
            # Binary search for next occurrence after current_pos
            positions = self.char_positions[char]
            idx = bisect.bisect_right(positions, current_pos)
            
            if idx == len(positions):
                return False
            
            current_pos = positions[idx]
        
        return True

EDGE CASES HANDLED:

1. Empty s: "" is subsequence of any string ✅
2. Empty t: Only "" is subsequence of "" ✅  
3. Single character: "b" in "abc" ✅
4. Repeated characters: "aa" in "aab" ✅
5. Same strings: "abc" in "abc" ✅
6. No match: "axc" in "ahbgdc" ✅

YOUR ORIGINAL BUG FIXED:

❌ ORIGINAL: char_index = idx
✅ FIXED: char_index += idx + 1

The bug was treating the relative index from find() as an absolute index.
Your fix correctly moves past the found character.

KEY TAKEAWAYS:
1. String find() returns relative index within substring
2. Two-pointer is the most efficient approach for this problem
3. For multiple queries, preprocessing can optimize performance
4. Always consider the follow-up requirements in interviews
5. Edge cases with empty strings are important to test

RECOMMENDATION:
- Current solution: Good and correct ✅
- For interviews: Learn two-pointer approach
- For follow-up: Implement preprocessing solution
- Your fix shows good debugging skills! 🎯
"""
