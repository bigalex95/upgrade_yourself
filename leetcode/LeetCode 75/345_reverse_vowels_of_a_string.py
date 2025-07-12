"""
Problem: 345. Reverse Vowels of a String
Difficulty: Easy
URL: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

Description:
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"



Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Reverse only the vowels in a string while keeping other characters in place.

        Uses a collect-reverse-replace approach: extract vowels, reverse them,
        then put them back in their original positions.

        Args:
            s: Input string containing letters and other characters

        Returns:
            str: String with vowels reversed, other characters unchanged
        """
        vowels = ["a", "e", "i", "o", "u"]
        vowels_in_str = []

        # Convert string to list for mutability
        s_list = list(s)

        for char in s_list:
            if char.lower() in vowels:
                vowels_in_str.append(char)

        vowels_in_str.reverse()
        vowel_idx = 0

        for i in range(len(s_list)):
            if s_list[i].lower() in vowels:
                s_list[i] = vowels_in_str[vowel_idx]
                vowel_idx += 1

        return "".join(s_list)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = "IceCreAm"  # Replace with actual input
    expected = "AceCreIm"  # Replace with expected output
    result = solution.reverseVowels(input1)
    print(f"Test 1: input1={input1},")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2 - Edge case
    input1 = "leetcode"  # Replace with actual input
    expected = "leotcede"  # Replace with expected output
    result = solution.reverseVowels(input1)
    print(f"Test 2: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3 - Mixed case vowels
    input1 = "Aa"
    expected = "aA"
    result = solution.reverseVowels(input1)
    print(f"Test 3: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 4 - No vowels
    input1 = "bcdfg"
    expected = "bcdfg"
    result = solution.reverseVowels(input1)
    print(f"Test 4: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 5 - Only vowels
    input1 = "aeiou"
    expected = "uoiea"
    result = solution.reverseVowels(input1)
    print(f"Test 5: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
YOUR SOLUTION ANALYSIS:
✅ Correct and works well!
✅ Easy to understand
✅ Time: O(n), Space: O(n)

APPROACH: Collect → Reverse → Replace
1. Extract all vowels from string
2. Reverse the vowel list  
3. Replace vowels in original positions

ALTERNATIVE SOLUTIONS:

# Approach 1: Your Current Solution (Collect-Reverse-Replace)
# Time: O(n), Space: O(n)
def reverseVowels_v1(self, s: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_str = []
    s_list = list(s)
    
    # Collect vowels
    for i in range(len(s_list)):
        if s_list[i].lower() in vowels:
            vowels_in_str.append(s_list[i])
    
    # Reverse and replace
    vowels_in_str.reverse()
    vowel_idx = 0
    
    for i in range(len(s_list)):
        if s_list[i].lower() in vowels:
            s_list[i] = vowels_in_str[vowel_idx]
            vowel_idx += 1
    
    return "".join(s_list)

# Approach 2: Two Pointers (Most Efficient)
# Time: O(n), Space: O(n) for list conversion
def reverseVowels_v2(self, s: str) -> str:
    vowels = set('aeiouAEIOU')  # Set for O(1) lookup
    s_list = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer to next vowel
        while left < right and s_list[left] not in vowels:
            left += 1
        
        # Move right pointer to previous vowel
        while left < right and s_list[right] not in vowels:
            right -= 1
        
        # Swap vowels
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    
    return ''.join(s_list)

# Approach 3: Stack-based (Clean and Intuitive)
# Time: O(n), Space: O(v) where v = number of vowels
def reverseVowels_v3(self, s: str) -> str:
    vowels = set('aeiouAEIOU')
    vowel_stack = []
    
    # Push all vowels to stack (LIFO = reversed order)
    for char in s:
        if char in vowels:
            vowel_stack.append(char)
    
    # Rebuild string, popping vowels from stack
    result = []
    for char in s:
        if char in vowels:
            result.append(vowel_stack.pop())
        else:
            result.append(char)
    
    return ''.join(result)

# Approach 4: Functional Style with Filter/Map
# Time: O(n), Space: O(n)
def reverseVowels_v4(self, s: str) -> str:
    vowels = set('aeiouAEIOU')
    vowel_chars = [c for c in s if c in vowels]
    vowel_chars.reverse()
    
    vowel_iter = iter(vowel_chars)
    return ''.join(next(vowel_iter) if c in vowels else c for c in s)

# Approach 5: Using String Indexing (Memory Optimized)
# Time: O(n), Space: O(v) where v = number of vowels
def reverseVowels_v5(self, s: str) -> str:
    vowels = 'aeiouAEIOU'
    vowel_chars = [c for c in s if c in vowels]
    vowel_chars.reverse()
    
    result = []
    vowel_index = 0
    
    for char in s:
        if char in vowels:
            result.append(vowel_chars[vowel_index])
            vowel_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

PERFORMANCE COMPARISON:

Approach 1 (Your Solution):
  ✅ Very readable and logical
  ✅ Easy to debug
  ❌ Uses list() + enumerate, slightly verbose

Approach 2 (Two Pointers):
  ✅ Most efficient - single pass
  ✅ Classic algorithm pattern
  ✅ In-place swapping
  ❌ Slightly more complex logic

Approach 3 (Stack):
  ✅ Most intuitive (stack naturally reverses)
  ✅ Clean separation of concerns
  ❌ Extra space for stack

Approach 4 (Functional):
  ✅ Very concise
  ✅ Pythonic style
  ❌ Can be harder to understand

Approach 5 (Optimized):
  ✅ Similar to yours but cleaner
  ✅ Good balance of readability/efficiency

RECOMMENDATIONS:
- Interviews: Approach 2 (Two Pointers) - shows algorithm knowledge
- Production: Approach 2 or 5 - most efficient
- Learning: Your approach (1) - easiest to understand and debug
- Python Style: Approach 4 - most Pythonic

OPTIMIZATIONS USED:
- set('aeiouAEIOU') instead of list for O(1) lookup
- Two pointers to avoid extra memory
- Iterator pattern for clean functional style
"""
