"""
Problem: 443. String Compression
Difficulty: Medium
URL: https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

Description:
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compress array of characters in-place using two pointers.

        APPROACH: Two-pointer technique
        - read: scans through original array to count characters
        - write: writes compressed result back to same array
        - Time: O(n), Space: O(1) - meets constant space requirement

        Key insight: We can safely overwrite the beginning of the array
        because we're always reading ahead of where we're writing.

        Args:
            chars: List of characters to compress in-place

        Returns:
            int: Length of compressed array (chars is modified in-place)
        """
        write = 0  # Position to write compressed data
        read = 0  # Position to read original data

        while read < len(chars):
            current_char = chars[read]
            count = 0

            # Count consecutive occurrences of current character
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            # Write the character to the array
            chars[write] = current_char
            write += 1

            # Write the count if > 1 (split multi-digit numbers)
            if count > 1:
                # Convert count to string and write each digit
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = ["a", "a", "b", "b", "c", "c", "c"]
    original1 = input1.copy()  # Keep original for display
    expected = 6
    result = solution.compress(input1)
    print(f"Test 1: Original={original1}")
    print(f"After compression: {input1[:result]}")
    print(f"Expected length: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input2 = ["a"]
    original2 = input2.copy()
    expected = 1
    result = solution.compress(input2)
    print(f"Test 2: Original={original2}")
    print(f"After compression: {input2[:result]}")
    print(f"Expected length: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3
    input3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    original3 = input3.copy()
    expected = 4
    result = solution.compress(input3)
    print(f"Test 3: Original={original3}")
    print(f"After compression: {input3[:result]}")
    print(f"Expected length: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 4 - Edge case with large numbers
    input4 = ["a"] * 100  # 100 'a's
    original4_info = f"[{'a'*100}] (100 'a's)"
    expected = 4  # "a" + "1" + "0" + "0"
    result = solution.compress(input4)
    print(f"Test 4: Original={original4_info}")
    print(f"After compression: {input4[:result]}")
    print(f"Expected length: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
YOUR ORIGINAL SOLUTION ANALYSIS:

ISSUES FOUND:
❌ NOT IN-PLACE: Creates new array s instead of modifying chars
❌ EXTRA SPACE: Violates O(1) space requirement  
❌ DOESN'T MODIFY INPUT: Original chars array unchanged
❌ MISUNDERSTOOD REQUIREMENTS: Problem explicitly says "stored in the input character array chars"

OPTIMAL SOLUTION EXPLANATION:

The key insight is using TWO POINTERS for in-place modification:

ALGORITHM: Two-Pointer In-Place Compression
1. read: Scans original data to count consecutive characters
2. write: Overwrites array with compressed data
3. Safe because we always read ahead of where we write

EXAMPLE WALKTHROUGH: ["a","a","b","b","c","c","c"]

Initial: chars = ['a','a','b','b','c','c','c'], write=0, read=0

Step 1: Count 'a's
- read=0,1: Found 2 'a's  
- chars[0] = 'a', chars[1] = '2'
- write=2, read=2
- State: ['a','2','b','b','c','c','c']

Step 2: Count 'b's  
- read=2,3: Found 2 'b's
- chars[2] = 'b', chars[3] = '2'  
- write=4, read=4
- State: ['a','2','b','2','c','c','c']

Step 3: Count 'c's
- read=4,5,6: Found 3 'c's
- chars[4] = 'c', chars[5] = '3'
- write=6, read=7
- Final: ['a','2','b','2','c','3','c'] → return 6

WHY IN-PLACE WORKS:
- We always read ahead of where we write (read ≥ write)
- Compressed data is always shorter than or equal to original
- Safe to overwrite because we've already processed those positions

ALTERNATIVE APPROACHES:

# Approach 1: Optimal Two-Pointer In-Place (CURRENT IMPLEMENTATION)
# Time: O(n), Space: O(1) ✅
def compress_v1(self, chars: List[str]) -> int:
    write = read = 0
    
    while read < len(chars):
        current_char = chars[read]
        count = 0
        
        # Count consecutive characters
        while read < len(chars) and chars[read] == current_char:
            read += 1
            count += 1
        
        # Write character
        chars[write] = current_char
        write += 1
        
        # Write count if > 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    
    return write

# Approach 2: Your Original (INCORRECT - Violates Requirements)  
# Time: O(n), Space: O(n) ❌
def compress_v2(self, chars: List[str]) -> int:
    s = [chars[0]]  # ❌ Extra space
    # ... creates new array instead of modifying chars ❌
    return len(s)   # ❌ chars unchanged

# Approach 3: Straightforward In-Place
# Time: O(n), Space: O(1) ✅
def compress_v3(self, chars: List[str]) -> int:
    if not chars:
        return 0
    
    write = 0
    i = 0
    
    while i < len(chars):
        current_char = chars[i]
        count = 0
        
        # Count consecutive occurrences
        while i < len(chars) and chars[i] == current_char:
            i += 1  
            count += 1
        
        # Write character
        chars[write] = current_char
        write += 1
        
        # Write count digits
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write] = digit
                write += 1
    
    return write

# Approach 4: Using Deque (Educational)
# Time: O(n), Space: O(1) ✅ 
def compress_v4(self, chars: List[str]) -> int:
    from collections import deque
    
    result_len = 0
    i = 0
    
    while i < len(chars):
        current_char = chars[i]
        count = 0
        
        while i < len(chars) and chars[i] == current_char:
            i += 1
            count += 1
        
        chars[result_len] = current_char
        result_len += 1
        
        if count > 1:
            # Use deque to handle multi-digit numbers
            digits = deque()
            while count:
                digits.appendleft(str(count % 10))
                count //= 10
            
            for digit in digits:
                chars[result_len] = digit
                result_len += 1
    
    return result_len

PERFORMANCE COMPARISON:

Approach 1 (Optimal Two-Pointer):
  ✅ O(n) time, O(1) space
  ✅ In-place modification  
  ✅ Clean and efficient
  ✅ Meets all requirements

Approach 2 (Your Original):
  ❌ O(n) time, O(n) space
  ❌ Creates extra array
  ❌ Doesn't modify input
  ❌ Violates problem requirements

Approach 3 (Straightforward):
  ✅ O(n) time, O(1) space
  ✅ In-place modification
  ✅ Easy to understand
  ✅ Alternative implementation

Approach 4 (Deque):
  ✅ O(n) time, O(1)* space
  ✅ In-place modification  
  ❌ More complex than needed
  ❌ *Deque uses small extra space

EDGE CASES HANDLED:

1. Single character: ["a"] → ["a"] (length 1)
2. No repetition: ["a","b","c"] → ["a","b","c"] (length 3)  
3. All same: ["a","a","a"] → ["a","3"] (length 2)
4. Large counts: 100 'a's → ["a","1","0","0"] (length 4)
5. Mixed: ["a","a","b","c","c","c"] → ["a","2","b","c","3"] (length 5)

KEY TAKEAWAYS:
1. Read problem requirements carefully (in-place modification!)
2. Two-pointer technique is powerful for in-place operations
3. Always consider space complexity constraints
4. In-place operations are safe when read pointer ≥ write pointer
5. Convert multi-digit numbers to individual character digits

FIXED ISSUES IN YOUR APPROACH:
✅ Implemented true in-place modification
✅ Eliminated extra space usage
✅ Original chars array now gets modified
✅ Meets O(1) space requirement  
✅ Added comprehensive test cases
✅ Handles multi-digit counts correctly
"""
