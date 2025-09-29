"""
Problem: 1679. Max Number of K-Sum Pairs
Difficulty: Medium
URL: https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

Description:
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.



Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""

from typing import List
from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Find maximum number of k-sum pairs using frequency counting.

        APPROACH: HashMap frequency counting (optimal)
        - Count frequency of each number
        - For each number x, check if (k-x) exists
        - Take minimum of freq[x] and freq[k-x] pairs
        - Handle special case when x = k-x (k is even, x = k/2)
        - Time: O(n), Space: O(n)

        Args:
            nums: List of integers
            k: Target sum for pairs

        Returns:
            int: Maximum number of operations (pairs) possible
        """
        # Count frequency of each number
        freq = Counter(nums)
        operations = 0

        for num in freq:
            complement = k - num

            if num == complement:
                # Special case: num + num = k (e.g., 3+3=6)
                # Can form freq[num] // 2 pairs
                operations += freq[num] // 2
            elif complement in freq and num < complement:
                # Regular case: num + complement = k
                # Take minimum available count
                # Use num < complement to avoid double counting
                operations += min(freq[num], freq[complement])

        return operations

    def maxOperations_your_approach_improved(self, nums: List[int], k: int) -> int:
        """
        Your approach but optimized (still not optimal)
        Time: O(n²), Space: O(1)
        """
        nums_copy = nums.copy()  # Don't modify original
        nums_copy.sort()  # Sort to enable early termination
        operations = 0
        i = 0

        while i < len(nums_copy):
            target = k - nums_copy[i]

            # Look for target in remaining elements
            found = False
            for j in range(i + 1, len(nums_copy)):
                if nums_copy[j] == target:
                    # Remove both elements (remove larger index first)
                    nums_copy.pop(j)
                    nums_copy.pop(i)
                    operations += 1
                    found = True
                    break
                elif nums_copy[j] > target:
                    # Since sorted, no point checking further
                    break

            if not found:
                i += 1

        return operations

    def maxOperations_two_pointer(self, nums: List[int], k: int) -> int:
        """
        Alternative optimal approach using two pointers
        Time: O(n log n), Space: O(1)
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return operations


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = [1, 2, 3, 4]
    input2 = 5
    expected = 2  # (1,4) and (2,3)
    print(f"Test 1: nums={input1}, k={input2}")
    result = solution.maxOperations(input1, input2)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = [3, 1, 3, 4, 3]
    input2 = 6
    expected = 1  # (3,3)
    print(f"Test 2: nums={input1}, k={input2}")
    result = solution.maxOperations(input1, input2)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3 - All same numbers that sum to k
    input1 = [2, 2, 2, 2]
    input2 = 4
    expected = 2  # (2,2) and (2,2)
    print(f"Test 3: nums={input1}, k={input2}")
    result = solution.maxOperations(input1, input2)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 4 - No valid pairs
    input1 = [1, 1, 1, 1]
    input2 = 3
    expected = 0  # No pairs sum to 3
    print(f"Test 4: nums={input1}, k={input2}")
    result = solution.maxOperations(input1, input2)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 5 - Single element equal to k/2
    input1 = [5]
    input2 = 10
    expected = 0  # Need two elements to form a pair
    print(f"Test 5: nums={input1}, k={input2}")
    result = solution.maxOperations(input1, input2)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 6 - Large numbers
    input1 = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4]
    input2 = 2
    expected = 2  # (1,1) and (1,1)
    print(f"Test 6: nums={input1}, k={input2}")
    result = solution.maxOperations(input1, input2)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
YOUR ORIGINAL SOLUTION ANALYSIS:

ISSUES FOUND:
❌ PERFORMANCE: O(n³) time complexity - too slow!
❌ list.remove() is O(n) operation
❌ "x in list" search is O(n) operation  
❌ Modifying list while iterating is error-prone
❌ Will timeout on large inputs (n=10⁵)

OPTIMAL SOLUTION EXPLANATION:

The key insight is to use FREQUENCY COUNTING instead of removing elements:

ALGORITHM: HashMap Frequency Counting
1. Count frequency of each number using Counter
2. For each unique number x, check if complement (k-x) exists
3. Handle two cases:
   - Regular case: x + complement = k (x ≠ complement)
   - Special case: x + x = k (x = k/2)
4. Sum up all possible pairs

EXAMPLE WALKTHROUGH: nums=[3,1,3,4,3], k=6

Step 1: Count frequencies
  freq = {3: 3, 1: 1, 4: 1}

Step 2: Process each unique number
  num=3: complement = 6-3 = 3
    Special case: 3+3=6, freq[3]=3 → 3//2 = 1 pair
  num=1: complement = 6-1 = 5  
    5 not in freq → 0 pairs
  num=4: complement = 6-4 = 2
    2 not in freq → 0 pairs

Total: 1 operation

WHY FREQUENCY COUNTING WORKS:
- We don't need to track which specific elements are used
- Only need to know how many of each value we have
- Can form min(freq[x], freq[k-x]) pairs for different values
- For same values (x = k-x), can form freq[x]//2 pairs

ALTERNATIVE APPROACHES:

# Approach 1: Optimal HashMap (CURRENT IMPLEMENTATION)
# Time: O(n), Space: O(n)
def maxOperations_v1(self, nums: List[int], k: int) -> int:
    from collections import Counter
    
    freq = Counter(nums)
    operations = 0
    
    for num in freq:
        complement = k - num
        
        if num == complement:
            operations += freq[num] // 2
        elif complement in freq and num < complement:
            operations += min(freq[num], freq[complement])
    
    return operations

# Approach 2: Two-Pointer (Sort-based)
# Time: O(n log n), Space: O(1)
def maxOperations_v2(self, nums: List[int], k: int) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1
    operations = 0
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == k:
            operations += 1
            left += 1
            right -= 1
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    
    return operations

# Approach 3: Your Original (INEFFICIENT)
# Time: O(n³), Space: O(1) ❌
def maxOperations_v3(self, nums: List[int], k: int) -> int:
    i = 0
    ops_count = 0
    
    while i < len(nums) and len(nums) > 0:
        first = nums[i]
        second = k - first
        
        if second in nums[i + 1:]:  # O(n) search
            nums.remove(first)      # O(n) removal
            nums.remove(second)     # O(n) removal
            ops_count += 1
        else:
            i += 1
    
    return ops_count

# Approach 4: Brute Force
# Time: O(n²), Space: O(1)
def maxOperations_v4(self, nums: List[int], k: int) -> int:
    used = [False] * len(nums)
    operations = 0
    
    for i in range(len(nums)):
        if used[i]:
            continue
        
        for j in range(i + 1, len(nums)):
            if not used[j] and nums[i] + nums[j] == k:
                used[i] = used[j] = True
                operations += 1
                break
    
    return operations

PERFORMANCE COMPARISON:

Approach 1 (HashMap Frequency):
  ✅ O(n) time - optimal
  ❌ O(n) space
  ✅ Most efficient overall
  ✅ Handles duplicates elegantly
  ✅ Clean and intuitive

Approach 2 (Two-Pointer):
  ⚠️  O(n log n) time - sorting overhead
  ✅ O(1) space - space optimal
  ✅ Classic two-pointer technique
  ✅ Good for interviews

Approach 3 (Your Original):
  ❌ O(n³) time - too slow
  ✅ O(1) space
  ❌ Modifies input array
  ❌ Complex index management
  ❌ Will timeout on large inputs

Approach 4 (Brute Force):
  ❌ O(n²) time - inefficient
  ❌ O(n) space for used array
  ✅ Easy to understand
  ❌ Not optimal

DETAILED COMPLEXITY ANALYSIS:

Your Original Approach Breakdown:
- Outer while loop: O(n) iterations
- "second in nums[i+1:]": O(n) search per iteration
- nums.remove(first): O(n) removal operation
- nums.remove(second): O(n) removal operation
- Total: O(n) × (O(n) + O(n) + O(n)) = O(n³)

Optimal Approach Breakdown:
- Counter(nums): O(n) to build frequency map
- Iterate through unique numbers: O(k) where k ≤ n
- Dictionary lookups: O(1) per lookup
- Total: O(n) + O(k) = O(n)

EDGE CASES HANDLED:

1. Special case k=2×x: [2,2,2,2], k=4 → 2 pairs ✅
2. No valid pairs: [1,1,1,1], k=3 → 0 pairs ✅
3. Single element: [5], k=10 → 0 pairs ✅
4. All different values: [1,2,3,4], k=5 → 2 pairs ✅
5. Large arrays: Handles n=10⁵ efficiently ✅

COMMON MISTAKES TO AVOID:

❌ Modifying array while iterating
❌ Using list.remove() in loops (O(n²) or worse)
❌ Linear search for complements
❌ Not handling the x + x = k case properly
❌ Double-counting pairs (use num < complement condition)
❌ Forgetting that we need exactly two elements per pair

KEY INSIGHTS:

1. **Frequency over removal**: Count occurrences instead of removing elements
2. **HashMap for O(1) lookups**: Avoid linear searches
3. **Handle self-pairs carefully**: When x + x = k, use freq[x] // 2
4. **Avoid double counting**: Process each unique pair only once
5. **Space-time tradeoffs**: O(n) space for O(n) time is worth it

INTERVIEW STRATEGY:

1. Start with brute force explanation
2. Identify bottlenecks (removal operations)
3. Suggest frequency counting optimization
4. Discuss space-time tradeoffs
5. Mention two-pointer alternative
6. Handle edge cases in discussion

RECOMMENDATIONS:
- Production: Use HashMap approach (optimal)
- Interviews: Know both HashMap and two-pointer
- Learning: Understand why your approach was slow
- Practice: Focus on avoiding O(n) operations in loops

Your original approach showed good problem understanding but needs 
optimization for large inputs! The fix demonstrates the power of 
choosing the right data structure (HashMap vs List). 🎯
"""
