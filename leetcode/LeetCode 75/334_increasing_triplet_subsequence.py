"""
Problem: 334. Increasing Triplet Subsequence
Difficulty: Medium
URL: https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

Description:
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such
that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

from typing import List
import sys


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Find if there exists an increasing triplet subsequence.

        OPTIMAL APPROACH: Track smallest and middle values
        - Time: O(n) - single pass
        - Space: O(1) - only two variables

        Key insight: We don't need actual indices, just track:
        - first: smallest number seen so far
        - second: smallest number greater than first
        - If we find any number > second, we have a triplet!

        Args:
            nums: List of integers

        Returns:
            bool: True if increasing triplet exists, False otherwise
        """

        # Initialize to infinity (largest possible values)
        first = sys.maxsize  # Smallest number seen so far
        second = sys.maxsize  # Smallest number > first

        for num in nums:
            if num <= first:
                # Update the smallest number
                first = num
            elif num <= second:
                # Update the middle number (num > first)
                second = num
            else:
                # Found a number > second (and second > first)
                # So we have: first < second < num
                return True

        return False

    def increasingTriplet_your_approach_fixed(self, nums: List[int]) -> bool:
        """
        Your three-pointer approach - FIXED version
        (kept for educational comparison)
        """
        n = len(nums)
        if n < 3:
            return False

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = [1, 2, 3, 4, 5]  # Replace with actual input
    expected = True  # Replace with expected output
    result = solution.increasingTriplet(input1)
    print(f"Test 1: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = [5, 4, 3, 2, 1]  # Replace with actual input
    expected = False  # Replace with expected output
    result = solution.increasingTriplet(input1)
    print(f"Test 2: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3 - Edge case
    input1 = [2, 1, 5, 0, 4, 6]  # Replace with actual input
    expected = True  # Replace with expected output
    result = solution.increasingTriplet(input1)
    print(f"Test 3: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 4 - Edge case
    input1 = [20, 100, 10, 12, 5, 13]  # Replace with actual input
    expected = True  # Replace with expected output
    result = solution.increasingTriplet(input1)
    print(f"Test 4: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 5 - Edge case
    input1 = [0, 4, 2, 1, 0, -1, -3]  # Replace with actual input
    expected = False  # Replace with expected output
    result = solution.increasingTriplet(input1)
    print(f"Test 5: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
YOUR ORIGINAL SOLUTION ANALYSIS:

ISSUES FOUND:
❌ IndexError: Array bounds not properly checked
❌ Complex Logic: Hard to follow pointer movements  
❌ Inefficient: Not optimal O(n) approach
❌ Debug prints: Left in production code
❌ Edge cases: Doesn't handle all scenarios correctly

OPTIMAL SOLUTION EXPLANATION:

The key insight is we don't need to track actual indices, just values:

ALGORITHM: Two-Variable Tracking
1. first = smallest number seen so far
2. second = smallest number > first  
3. If we find any number > second → triplet found!

EXAMPLE WALKTHROUGH: [2, 1, 5, 0, 4, 6]

Initial: first = ∞, second = ∞

num = 2: 2 ≤ ∞ → first = 2
num = 1: 1 ≤ 2 → first = 1  
num = 5: 5 > 1, 5 ≤ ∞ → second = 5
num = 0: 0 ≤ 1 → first = 0
num = 4: 4 > 0, 4 ≤ 5 → second = 4  
num = 6: 6 > 4 → FOUND! (first=0 < second=4 < current=6)

WHY THIS WORKS:
- We maintain the smallest possible values for first two positions
- When we find a third value larger than both, we have our triplet
- Even if first gets updated later, we've already "locked in" a valid sequence

ALTERNATIVE APPROACHES:

# Approach 1: Optimal Two-Variable (CURRENT IMPLEMENTATION)
# Time: O(n), Space: O(1)
def increasingTriplet_v1(self, nums: List[int]) -> bool:
    import sys
    first = second = sys.maxsize
    
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

# Approach 2: Brute Force (Your fixed approach)
# Time: O(n³), Space: O(1)
def increasingTriplet_v2(self, nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] < nums[j] < nums[k]:
                    return True
    return False

# Approach 3: Left/Right Min/Max Arrays
# Time: O(n), Space: O(n)
def increasingTriplet_v3(self, nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False
    
    # left_min[i] = minimum value to the left of i
    left_min = [0] * n
    left_min[0] = nums[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], nums[i])
    
    # right_max[i] = maximum value to the right of i  
    right_max = [0] * n
    right_max[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], nums[i])
    
    # Check for triplet
    for i in range(1, n-1):
        if left_min[i-1] < nums[i] < right_max[i+1]:
            return True
    
    return False

# Approach 4: Stack-based
# Time: O(n), Space: O(n)
def increasingTriplet_v4(self, nums: List[int]) -> bool:
    stack = []
    
    for num in nums:
        # Remove elements from stack that are >= current number
        while stack and stack[-1] >= num:
            stack.pop()
        
        stack.append(num)
        
        if len(stack) >= 3:
            return True
    
    return False

# Approach 5: Binary Search
# Time: O(n log n), Space: O(n)
def increasingTriplet_v5(self, nums: List[int]) -> bool:
    import bisect
    tails = []
    
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
        
        if len(tails) >= 3:
            return True
    
    return False

PERFORMANCE COMPARISON:

Approach 1 (Optimal Two-Variable):
  ✅ O(n) time, O(1) space
  ✅ Most efficient 
  ✅ Clean and elegant
  ✅ Handles all edge cases

Approach 2 (Brute Force):
  ❌ O(n³) time - too slow
  ✅ Easy to understand
  ✅ Guaranteed correct

Approach 3 (Left/Right Arrays):
  ✅ O(n) time
  ❌ O(n) space
  ✅ Very intuitive logic
  ✅ Good for learning

Approach 4 (Stack):
  ✅ O(n) time  
  ❌ O(n) space
  ❌ Incorrect for this problem

Approach 5 (Binary Search):
  ❌ O(n log n) time
  ❌ O(n) space
  ✅ Shows LIS knowledge

RECOMMENDATIONS:
- Production: Approach 1 (optimal)
- Interviews: Approach 1 or 3 (show optimization thinking)
- Learning: Start with Approach 2, evolve to 1

KEY TAKEAWAYS:
1. Sometimes you don't need to track actual positions/indices
2. Greedy algorithms can be very powerful
3. Two-variable tracking is a common optimization pattern
4. Always check edge cases and array bounds!

FIXED ISSUES IN YOUR APPROACH:
✅ Removed debug prints
✅ Fixed index out of bounds
✅ Implemented optimal O(n) solution
✅ Added proper documentation
✅ Corrected test case expectations
"""
