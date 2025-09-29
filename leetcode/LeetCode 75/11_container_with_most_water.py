"""
Problem: 11. Container With Most Water
Difficulty: Medium
URL: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find maximum water area using two-pointer technique.

        APPROACH: Two-pointer greedy algorithm
        - Start with widest possible container (left=0, right=n-1)
        - Always move the pointer with smaller height inward
        - Keep track of maximum area found so far
        - Time: O(n), Space: O(1)

        Key insight: Moving the taller line inward can never give a better result
        because the height is limited by the shorter line and width decreases.

        Args:
            height: List of integers representing line heights

        Returns:
            int: Maximum water area that can be contained
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current container dimensions
            container_height = min(height[left], height[right])
            container_width = right - left
            current_area = container_height * container_width

            # Update maximum area if current is larger
            max_area = max(max_area, current_area)

            # Move pointer with smaller height (greedy choice)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected = 49  # Between indices 1 and 6 (heights 8 and 8, width 5)
    result = solution.maxArea(input1)
    print(f"Test 1: height={input1}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input2 = [1, 1]
    expected = 1  # Only one possible container
    result = solution.maxArea(input2)
    print(f"Test 2: height={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3 - Ascending heights
    input3 = [1, 2, 3, 4, 5]
    expected = 6  # Between indices 0 and 4 (heights 1 and 5, width 4)
    result = solution.maxArea(input3)
    print(f"Test 3: height={input3}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 4 - Descending heights
    input4 = [5, 4, 3, 2, 1]
    expected = 6  # Between indices 0 and 4 (heights 5 and 1, width 4)
    result = solution.maxArea(input4)
    print(f"Test 4: height={input4}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 5 - Equal heights
    input5 = [3, 3, 3, 3]
    expected = 9  # Between indices 0 and 3 (heights 3 and 3, width 3)
    result = solution.maxArea(input5)
    print(f"Test 5: height={input5}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 6 - Large difference in heights
    input6 = [1, 1000, 1000, 1]
    expected = 1000  # Between indices 1 and 2 (heights 1000 and 1000, width 1)
    result = solution.maxArea(input6)
    print(f"Test 6: height={input6}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
YOUR SOLUTION ANALYSIS:

ALGORITHM: Two-Pointer Greedy Approach ✅
✅ CORRECT: Passes all test cases
✅ OPTIMAL: O(n) time complexity  
✅ EFFICIENT: O(1) space complexity
✅ WELL-IMPLEMENTED: Clean and logical

IMPROVEMENTS MADE:
✅ Fixed variable naming (max_height → container_height, max_weight → container_width)
✅ Simplified max area update (used max() function)
✅ Added comprehensive documentation
✅ Improved code readability

ALGORITHM EXPLANATION:

The two-pointer approach works on a key insight:

KEY INSIGHT: Moving the taller line inward can NEVER improve the result
- Area = min(height[left], height[right]) × (right - left)  
- The height is constrained by the shorter line
- Moving inward always decreases width
- So moving the taller line only decreases area

GREEDY STRATEGY: Always move the pointer with the smaller height
- This gives the best chance of finding a taller line
- We don't miss any potentially better solutions

EXAMPLE WALKTHROUGH: [1,8,6,2,5,4,8,3,7]

Initial: left=0(h=1), right=8(h=7) → area = min(1,7) × 8 = 8
Step 1: Move left (1 < 7) → left=1(h=8), right=8(h=7) → area = 7×7 = 49 ⭐
Step 2: Move right (8 > 7) → left=1(h=8), right=7(h=3) → area = 3×6 = 18
...continue until left meets right

Maximum found: 49 (between heights 8 and 7 with width 7)

WHY THIS WORKS:

Mathematical Proof Sketch:
1. Start with the widest possible container
2. At each step, we eliminate one line from consideration
3. We choose to eliminate the shorter line because:
   - Any container using this shorter line with a narrower width
   - Will have area ≤ current area (same height, less width)
4. By always eliminating the "worse" choice, we never miss the optimal solution

ALTERNATIVE APPROACHES:

# Approach 1: Optimal Two-Pointer (CURRENT IMPLEMENTATION)
# Time: O(n), Space: O(1) ✅
def maxArea_v1(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Approach 2: Brute Force (INEFFICIENT)
# Time: O(n²), Space: O(1) ❌
def maxArea_v2(self, height: List[int]) -> int:
    max_area = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
    
    return max_area

# Approach 3: Divide and Conquer (OVERCOMPLICATED)
# Time: O(n log n), Space: O(log n) ❌
def maxArea_v3(self, height: List[int]) -> int:
    def divide_conquer(left, right):
        if left >= right:
            return 0
        
        if right - left == 1:
            return min(height[left], height[right]) * 1
        
        mid = (left + right) // 2
        
        # Check cross-boundary cases
        max_cross = 0
        for i in range(left, mid + 1):
            for j in range(mid + 1, right + 1):
                area = min(height[i], height[j]) * (j - i)
                max_cross = max(max_cross, area)
        
        # Recursively solve subproblems
        left_max = divide_conquer(left, mid)
        right_max = divide_conquer(mid + 1, right)
        
        return max(max_cross, left_max, right_max)
    
    return divide_conquer(0, len(height) - 1)

# Approach 4: Dynamic Programming (OVERKILL)
# Time: O(n²), Space: O(n²) ❌
def maxArea_v4(self, height: List[int]) -> int:
    n = len(height)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = min(height[i], height[j]) * (j - i)
    
    return max(max(row) for row in dp)

PERFORMANCE COMPARISON:

Approach 1 (Two-Pointer):
  ✅ O(n) time - optimal
  ✅ O(1) space - optimal  
  ✅ Single pass algorithm
  ✅ Greedy and elegant
  ✅ Industry standard solution

Approach 2 (Brute Force):
  ❌ O(n²) time - too slow
  ✅ O(1) space
  ✅ Easy to understand
  ❌ Times out on large inputs

Approach 3 (Divide & Conquer):
  ❌ O(n log n) time - worse than optimal
  ❌ O(log n) space
  ❌ Overcomplicated
  ❌ No advantage over brute force

Approach 4 (Dynamic Programming):
  ❌ O(n²) time - inefficient
  ❌ O(n²) space - memory intensive
  ❌ Unnecessary for this problem
  ❌ Solves subproblems we don't need

WHY TWO-POINTER IS OPTIMAL:

1. **Completeness**: Examines all potentially optimal solutions
2. **Efficiency**: Each element visited at most once  
3. **Greedy Insight**: Never eliminates the optimal solution
4. **Space Optimal**: Only uses constant extra space
5. **Intuitive**: Logical decision at each step

EDGE CASES HANDLED:

1. Minimum input: [a, b] → area = min(a,b) × 1 ✅
2. Equal heights: [3,3,3,3] → max width gives max area ✅  
3. Ascending: [1,2,3,4,5] → end points often optimal ✅
4. Descending: [5,4,3,2,1] → end points often optimal ✅
5. Large differences: [1,1000,1000,1] → close high points ✅
6. All same: [5,5,5,5,5] → max width optimal ✅

COMMON MISTAKES TO AVOID:

❌ Moving both pointers simultaneously
❌ Moving the taller pointer first  
❌ Not considering the width factor
❌ Trying to use complex data structures
❌ Over-engineering with divide-and-conquer
❌ Confusing this with "trapping rainwater" problem

KEY TAKEAWAYS:

1. **Two-pointer technique** is powerful for optimization problems
2. **Greedy algorithms** can be optimal when the greedy choice is correct
3. **Mathematical insight** often leads to elegant solutions  
4. **Simple approaches** are often better than complex ones
5. **Understanding the problem constraints** guides algorithm choice

INTERVIEW TIPS:

1. Start with brute force explanation (O(n²))
2. Identify the key insight about moving pointers
3. Explain why moving the shorter pointer is optimal
4. Implement clean two-pointer solution
5. Discuss time/space complexity
6. Handle edge cases in your explanation

Your solution demonstrates excellent algorithmic thinking! 🎯
"""
