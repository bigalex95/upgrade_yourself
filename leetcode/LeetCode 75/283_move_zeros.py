"""
Problem: 283. Move Zeroes
Difficulty: Easy
URL: https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

Description:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeros to the end while maintaining relative order of non-zeros.

        APPROACH: Two-pointer technique
        - left: points to position where next non-zero should go
        - right: scans through array to find non-zeros
        - Time: O(n), Space: O(1)

        Key insight: We collect all non-zeros at the beginning,
        then fill the rest with zeros.

        Args:
            nums: List of integers to modify in-place

        Returns:
            None: Modifies nums in-place
        """
        if len(nums) <= 1:
            return
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = [0, 1, 0, 3, 12]
    original1 = input1.copy()  # Keep original for display
    expected1 = [1, 3, 12, 0, 0]  # Expected result after modification
    result = solution.moveZeroes(input1)  # This modifies input1 in-place
    print(f"Test 1: Original={original1}")
    print(f"After moveZeroes: {input1}")
    print(f"Expected: {expected1}")
    print(f"Return value: {result} (should be None)")
    print(f"Pass: {input1 == expected1}\n")

    # Test case 2
    input2 = [0]
    original2 = input2.copy()
    expected2 = [0]
    result = solution.moveZeroes(input2)
    print(f"Test 2: Original={original2}")
    print(f"After moveZeroes: {input2}")
    print(f"Expected: {expected2}")
    print(f"Return value: {result} (should be None)")
    print(f"Pass: {input2 == expected2}\n")

    # Test case 3 - All zeros
    input3 = [0, 0, 0]
    original3 = input3.copy()
    expected3 = [0, 0, 0]
    result = solution.moveZeroes(input3)
    print(f"Test 3: Original={original3}")
    print(f"After moveZeroes: {input3}")
    print(f"Expected: {expected3}")
    print(f"Return value: {result} (should be None)")
    print(f"Pass: {input3 == expected3}\n")

    # Test case 4 - No zeros
    input4 = [1, 2, 3]
    original4 = input4.copy()
    expected4 = [1, 2, 3]
    result = solution.moveZeroes(input4)
    print(f"Test 4: Original={original4}")
    print(f"After moveZeroes: {input4}")
    print(f"Expected: {expected4}")
    print(f"Return value: {result} (should be None)")
    print(f"Pass: {input4 == expected4}\n")

    # Test case 5 - Single non-zero
    input5 = [1]
    original5 = input5.copy()
    expected5 = [1]
    result = solution.moveZeroes(input5)
    print(f"Test 5: Original={original5}")
    print(f"After moveZeroes: {input5}")
    print(f"Expected: {expected5}")
    print(f"Return value: {result} (should be None)")
    print(f"Pass: {input5 == expected5}\n")


if __name__ == "__main__":
    test_solution()


"""
HOW TO TEST IN-PLACE FUNCTIONS THAT RETURN None:

PROBLEM: Functions that modify arrays in-place return None, so you can't test the return value.
SOLUTION: Test the modified array state instead!

TESTING PATTERN:
1. Create test input array
2. Keep a copy of original for display  
3. Call the function (modifies array in-place)
4. Compare modified array with expected result
5. Verify return value is None

EXAMPLE:
    input_array = [0, 1, 0, 3, 12]
    original = input_array.copy()  # Keep for display
    expected = [1, 3, 12, 0, 0]    # What we expect after modification
    
    result = solution.moveZeroes(input_array)  # Modifies input_array
    
    # Test the modified array, not the return value
    assert input_array == expected  
    assert result is None

ALGORITHM EXPLANATION:

The key insight is using TWO POINTERS for in-place modification:

APPROACH: Two-Pointer Collection
1. left: Position where next non-zero should go
2. right: Scans through array to find non-zeros  
3. Collect all non-zeros at front, fill rest with zeros

EXAMPLE WALKTHROUGH: [0, 1, 0, 3, 12]

Phase 1: Collect non-zeros at front
  left=0, right=0: nums[0]=0 (skip, left stays 0)
  left=0, right=1: nums[1]=1 → move to position 0, left=1
  left=1, right=2: nums[2]=0 (skip, left stays 1)  
  left=1, right=3: nums[3]=3 → move to position 1, left=2
  left=2, right=4: nums[4]=12 → move to position 2, left=3
  
  Result: [1, 3, 12, ?, ?], left=3

Phase 2: Fill remaining with zeros
  Fill positions 3,4 with 0: [1, 3, 12, 0, 0]

WHY THIS WORKS:
- We preserve relative order of non-zeros
- All zeros naturally end up at the end
- O(n) time with single pass
- O(1) space with only two pointers

ALTERNATIVE APPROACHES:

# Approach 1: Optimal Two-Pointer (CURRENT IMPLEMENTATION)
# Time: O(n), Space: O(1)
def moveZeroes_v1(self, nums: List[int]) -> None:
    left = 0
    
    # Collect non-zeros at front
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
    
    # Fill rest with zeros
    while left < len(nums):
        nums[left] = 0
        left += 1

# Approach 2: Swap-based Two-Pointer 
# Time: O(n), Space: O(1)
def moveZeroes_v2(self, nums: List[int]) -> None:
    left = 0
    
    for right in range(len(nums)):
        if nums[right] != 0:
            # Swap non-zero to front
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

# Approach 3: Remove and Append (LESS EFFICIENT)
# Time: O(n²), Space: O(1) 
def moveZeroes_v3(self, nums: List[int]) -> None:
    zero_count = 0
    i = 0
    
    # Remove zeros and count them
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            zero_count += 1
        else:
            i += 1
    
    # Append zeros at end
    nums.extend([0] * zero_count)

# Approach 4: Create New Array (VIOLATES IN-PLACE REQUIREMENT)
# Time: O(n), Space: O(n) ❌
def moveZeroes_v4(self, nums: List[int]) -> None:
    non_zeros = [x for x in nums if x != 0]  # ❌ Extra space
    zeros = [0] * (len(nums) - len(non_zeros))
    result = non_zeros + zeros
    
    # Copy back (this is allowed for in-place requirement)
    for i in range(len(nums)):
        nums[i] = result[i]

PERFORMANCE COMPARISON:

Approach 1 (Two-Pointer Collection):
  ✅ O(n) time, O(1) space
  ✅ Single pass through array
  ✅ Minimal operations
  ✅ Easy to understand

Approach 2 (Swap-based):
  ✅ O(n) time, O(1) space  
  ✅ Single pass through array
  ✅ Slightly more operations (swaps)
  ✅ Preserves order differently

Approach 3 (Remove/Append):
  ❌ O(n²) time in worst case
  ✅ O(1) space
  ❌ List operations are expensive
  ❌ Not optimal

Approach 4 (New Array):
  ✅ O(n) time
  ❌ O(n) space
  ❌ Violates spirit of in-place
  ❌ Not optimal

EDGE CASES HANDLED:

1. All zeros: [0,0,0] → [0,0,0]
2. No zeros: [1,2,3] → [1,2,3]  
3. Single element: [0] → [0], [1] → [1]
4. Already sorted: [1,2,0,0] → [1,2,0,0]
5. Alternating: [0,1,0,1] → [1,1,0,0]

FOLLOW-UP: MINIMIZE OPERATIONS

The current solution minimizes operations by:
1. Single pass through array (O(n) time)
2. Only writing when necessary (collect phase)
3. Bulk zero-filling at end
4. No unnecessary swaps or moves

This is optimal for the follow-up requirement!

KEY TAKEAWAYS:
1. Test in-place functions by checking array state, not return value
2. Two-pointer technique is powerful for in-place array problems  
3. Collect-then-fill pattern works well for partitioning problems
4. Always preserve relative order when required
5. Consider follow-up requirements for optimization

TESTING BEST PRACTICES FOR IN-PLACE FUNCTIONS:
✅ Save original array for display
✅ Test modified array against expected result
✅ Verify return value is None/void
✅ Include edge cases (empty, single element, all same)
✅ Test boundary conditions
"""
