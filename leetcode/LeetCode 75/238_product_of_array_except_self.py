"""
Problem: 238. Product of Array Except Self
Difficulty: Medium
URL: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate product of all elements except self for each position.

        OPTIMAL APPROACH: Two-pass with left and right products
        - Time: O(n) - Efficient for large inputs
        - Space: O(1) - Only uses output array

        Key insight: result[i] = (left products) × (right products)

        Args:
            nums: List of integers

        Returns:
            List[int]: Product of all elements except self at each position
        """
        n = len(nums)
        result = [1] * n

        # First pass: calculate left products
        # result[i] = product of all elements to the left of i
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Second pass: multiply by right products
        # result[i] *= product of all elements to the right of i
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result

    def productExceptSelf_brute_force(self, nums: List[int]) -> List[int]:
        """
        ORIGINAL SOLUTION (KEPT FOR REFERENCE)
        ⚠️  O(n²) time complexity - too slow for large inputs!
        """
        result = []
        mul_result = 1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    mul_result *= nums[j]
            result.append(mul_result)
            mul_result = 1

        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = [1, 2, 3, 4]  # Replace with actual input
    expected = [24, 12, 8, 6]  # Replace with expected output
    result = solution.productExceptSelf(input1)
    print(f"Test 1: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = [-1, 1, 0, -3, 3]  # Replace with actual input
    expected = [0, 0, 9, 0, 0]  # Replace with expected output
    result = solution.productExceptSelf(input1)
    print(f"Test 2: input1={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
SOLUTION ANALYSIS:

YOUR CURRENT SOLUTION:
✅ Correct: Produces right answers
❌ Time Complexity: O(n²) - TOO SLOW for large inputs!
✅ Space Complexity: O(1) - Good
❌ Will get Time Limit Exceeded on LeetCode

PROBLEM: Your nested loop approach recalculates products unnecessarily
For array [1,2,3,4]:
- Position 0: calculates 2×3×4 = 24
- Position 1: calculates 1×3×4 = 12  
- Position 2: calculates 1×2×4 = 8
- Position 3: calculates 1×2×3 = 6

OPTIMAL APPROACHES:

# Approach 1: Two-Pass Left/Right Products (RECOMMENDED)
# Time: O(n), Space: O(1)
def productExceptSelf_v1(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    
    # Pass 1: Left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Pass 2: Right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# Approach 2: Separate Left/Right Arrays (Easier to understand)
# Time: O(n), Space: O(n)
def productExceptSelf_v2(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left = [1] * n
    right = [1] * n
    result = [1] * n
    
    # Calculate left products
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    
    # Calculate right products
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    
    # Combine left and right
    for i in range(n):
        result[i] = left[i] * right[i]
    
    return result

# Approach 3: Division-based (NOT ALLOWED by problem, but worth knowing)
# Time: O(n), Space: O(1)
def productExceptSelf_v3(self, nums: List[int]) -> List[int]:
    # ❌ Problem specifically says "without using division"
    total_product = 1
    zero_count = 0
    
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num
    
    result = []
    for num in nums:
        if zero_count > 1:
            result.append(0)
        elif zero_count == 1:
            result.append(total_product if num == 0 else 0)
        else:
            result.append(total_product // num)
    
    return result

# Approach 4: Prefix/Suffix Products (Same as v1, different perspective)
# Time: O(n), Space: O(1)
def productExceptSelf_v4(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [0] * n
    
    # answer[i] contains the product of all elements to the left of i
    answer[0] = 1
    for i in range(1, n):
        answer[i] = nums[i - 1] * answer[i - 1]
    
    # R contains the product of all elements to the right of i
    R = 1
    for i in reversed(range(n)):
        answer[i] = answer[i] * R
        R *= nums[i]
    
    return answer

STEP-BY-STEP EXAMPLE: [1,2,3,4]

Approach 1 (Optimal):
Initial: result = [1, 1, 1, 1]

Pass 1 (Left products):
i=0: result[0] = 1, left_product = 1×1 = 1
i=1: result[1] = 1, left_product = 1×2 = 2  
i=2: result[2] = 2, left_product = 2×3 = 6
i=3: result[3] = 6, left_product = 6×4 = 24
Result after pass 1: [1, 1, 2, 6]

Pass 2 (Right products):
i=3: result[3] = 6×1 = 6, right_product = 1×4 = 4
i=2: result[2] = 2×4 = 8, right_product = 4×3 = 12
i=1: result[1] = 1×12 = 12, right_product = 12×2 = 24
i=0: result[0] = 1×24 = 24, right_product = 24×1 = 24
Final result: [24, 12, 8, 6] ✅

PERFORMANCE COMPARISON:

Your Solution (Brute Force):
  ✅ Correct results
  ❌ O(n²) time - fails on large inputs
  ✅ O(1) space
  ❌ Not acceptable for LeetCode

Approach 1 (Optimal):
  ✅ O(n) time - efficient
  ✅ O(1) space (excluding output)
  ✅ Meets all problem requirements
  ✅ Most elegant solution

Approach 2 (Clear):
  ✅ O(n) time
  ❌ O(n) extra space
  ✅ Easier to understand logic
  ✅ Good for learning

RECOMMENDATION:
Replace your current solution with Approach 1 (productExceptSelf_optimal).
It's the standard LeetCode solution that passes all test cases efficiently.

KEY INSIGHT:
Instead of recalculating products from scratch for each position,
pre-compute left and right products to avoid redundant calculations.
"""
