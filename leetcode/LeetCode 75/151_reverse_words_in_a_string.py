"""
Problem: 151. Reverse Words in a String
Difficulty: Medium
URL: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

Description:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.


Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of words in a string, handling multiple spaces correctly.

        Uses Python's built-in string methods for an elegant solution:
        - strip() removes leading/trailing spaces
        - split() splits on any whitespace and removes empty strings
        - [::-1] reverses the word list
        - join() combines with single spaces

        Args:
            s: Input string with words separated by spaces

        Returns:
            str: String with words in reverse order, single spaces between words
        """
        # Split the string by whitespace, filter out empty strings, reverse the list, and join with a single space
        words = s.strip().split()
        # Handles leading/trailing/multiple spaces automatically
        reversed_words = words[::-1]  # Clean reversal using slicing
        return " ".join(reversed_words)  # Single space joining


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = "the sky is blue"  # Replace with actual input
    expected = "blue is sky the"  # Replace with expected output
    result = solution.reverseWords(input1)
    print(f"Test 1: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = "  hello world  "  # Replace with actual input
    expected = "world hello"  # Replace with expected output
    result = solution.reverseWords(input1)
    print(f"Test 2: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3
    input1 = "a good   example"  # Replace with actual input
    expected = "example good a"  # Replace with expected output
    result = solution.reverseWords(input1)
    print(f"Test 3: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 4 - Single word
    input1 = "hello"
    expected = "hello"
    result = solution.reverseWords(input1)
    print(f"Test 4: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 5 - Multiple spaces everywhere
    input1 = "  a   b   c  "
    expected = "c b a"
    result = solution.reverseWords(input1)
    print(f"Test 5: input1='{input1}'")
    print(f"Expected: '{expected}', Got: '{result}'")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
YOUR SOLUTION ANALYSIS:
✅ Perfect! Elegant and Pythonic
✅ Handles all edge cases correctly
✅ Time: O(n), Space: O(n)
✅ Very readable and concise

APPROACH: Strip → Split → Reverse → Join
1. Remove leading/trailing spaces with strip()
2. Split on whitespace (automatically handles multiple spaces)
3. Reverse the word list with slicing [::-1]
4. Join with single spaces

ALTERNATIVE SOLUTIONS:

# Approach 1: Your Solution (Pythonic - RECOMMENDED)
# Time: O(n), Space: O(n)
def reverseWords_v1(self, s: str) -> str:
    words = s.strip().split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# One-liner version:
def reverseWords_v1_oneliner(self, s: str) -> str:
    return " ".join(s.strip().split()[::-1])

# Approach 2: Manual Parsing (Interview-friendly)
# Time: O(n), Space: O(n)
def reverseWords_v2(self, s: str) -> str:
    words = []
    word = ""
    
    for char in s:
        if char != ' ':
            word += char
        elif word:  # If we have a word and hit a space
            words.append(word)
            word = ""
    
    if word:  # Don't forget the last word
        words.append(word)
    
    # Reverse and join
    return " ".join(words[::-1])

# Approach 3: Two-pass with manual space handling
# Time: O(n), Space: O(n)
def reverseWords_v3(self, s: str) -> str:
    # First pass: extract words
    words = []
    i = 0
    n = len(s)
    
    while i < n:
        # Skip spaces
        while i < n and s[i] == ' ':
            i += 1
        
        if i >= n:
            break
            
        # Extract word
        start = i
        while i < n and s[i] != ' ':
            i += 1
        
        words.append(s[start:i])
    
    # Second pass: reverse and join
    return " ".join(words[::-1])

# Approach 4: Stack-based (Natural reversal)
# Time: O(n), Space: O(n)
def reverseWords_v4(self, s: str) -> str:
    stack = []
    word = ""
    
    for char in s + " ":  # Add space to handle last word
        if char != ' ':
            word += char
        elif word:
            stack.append(word)
            word = ""
    
    return " ".join(stack[::-1])

# Approach 5: Regex-based (Clean but requires import)
# Time: O(n), Space: O(n)
def reverseWords_v5(self, s: str) -> str:
    import re
    words = re.findall(r'\\S+', s)  # Find all non-whitespace sequences
    return " ".join(words[::-1])

# Approach 6: In-place simulation (For follow-up question)
# Time: O(n), Space: O(n) - Python strings are immutable, so truly O(1) space impossible
def reverseWords_v6(self, s: str) -> str:
    # Convert to list for "in-place" operations
    chars = list(s.strip())
    n = len(chars)
    
    # Step 1: Reverse entire string
    chars.reverse()
    
    # Step 2: Reverse each word back to correct order
    start = 0
    for i in range(n + 1):
        if i == n or chars[i] == ' ':
            # Reverse word from start to i-1
            chars[start:i] = chars[start:i][::-1]
            start = i + 1
    
    # Step 3: Handle multiple spaces (convert to single spaces)
    result = []
    i = 0
    while i < n:
        if chars[i] != ' ':
            result.append(chars[i])
        else:
            if result and result[-1] != ' ':
                result.append(' ')
        i += 1
    
    return ''.join(result).strip()

PERFORMANCE COMPARISON:

Approach 1 (Your Solution):
  ✅ Most Pythonic and readable
  ✅ Leverages built-in optimized methods
  ✅ Handles edge cases automatically
  ✅ Shortest and cleanest code

Approach 2 (Manual Parsing):
  ✅ Shows understanding of string processing
  ✅ Good for interviews (demonstrates logic)
  ❌ More verbose and error-prone

Approach 3 (Two-pass):
  ✅ Clear separation of concerns
  ✅ Easy to debug
  ❌ More complex than needed

Approach 4 (Stack):
  ✅ Natural use of stack for reversal
  ✅ Easy to understand conceptually
  ❌ Slightly more memory overhead

Approach 5 (Regex):
  ✅ Very concise
  ❌ Requires regex knowledge
  ❌ Might be overkill for this problem

Approach 6 (In-place simulation):
  ✅ Addresses the follow-up question
  ✅ Shows advanced algorithm knowledge
  ❌ Complex and hard to get right
  ❌ Not truly O(1) space in Python

FOLLOW-UP ANALYSIS:
The follow-up asks about O(1) extra space, which is impossible in Python since strings 
are immutable. In languages like C++ with mutable strings, you could:
1. Reverse the entire string
2. Reverse each word individually
3. Remove extra spaces in-place

RECOMMENDATIONS:
- Production code: Your solution (Approach 1) - most reliable and readable
- Interviews: Your solution or Approach 2 - shows both efficiency and understanding
- Learning: Try Approach 2 to understand manual parsing
- Advanced: Approach 6 for algorithm depth

YOUR SOLUTION VERDICT: 🏆 PERFECT
- Leverages Python's strengths
- Handles all edge cases
- Clean and maintainable
- Optimal time/space complexity
"""
