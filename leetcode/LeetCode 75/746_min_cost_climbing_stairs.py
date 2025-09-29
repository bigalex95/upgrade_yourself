"""
Problem: 746. Min Cost Climbing Stairs
Difficulty: Easy
URL: https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75

Description:
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Find the minimum cost to reach the top of the stairs using space-optimized DP.

        You can start from index 0 or 1, and from each step you can climb 1 or 2 steps.
        The goal is to reach beyond the last step with minimum cost.

        Uses a space-optimized approach that only tracks the minimum cost to reach
        the previous two steps, sliding the window as we progress.

        Args:
            cost: List of integers representing cost of each step (2 <= len <= 1000)

        Returns:
            int: Minimum cost to reach the top of the stairs

        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - only use two variables to track previous costs
        """
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            a, b = b, cost[i] + min(a, b)

        return min(a, b)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = [10, 15, 20]  # Replace with actual input
    expected = 15  # Replace with expected output
    print(f"Test 1: input1={input1}")
    result = solution.minCostClimbingStairs(input1)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  # Replace with actual input
    expected = 6  # Replace with expected output
    print(f"Test 2: input1={input1}")
    result = solution.minCostClimbingStairs(input1)
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
ALTERNATIVE APPROACHES AND ANALYSIS:

This is a classic dynamic programming problem where we need to find the minimum cost
to reach the top of stairs. Your current solution is optimal!

PROBLEM ANALYSIS:
- Can start from index 0 or 1 (both have cost cost[0] and cost[1] respectively)
- From any step i, can climb to step i+1 or i+2
- Goal: reach beyond the last step (index len(cost)) with minimum total cost
- DP recurrence: dp[i] = cost[i] + min(dp[i-1], dp[i-2])

APPROACH 1: SPACE-OPTIMIZED DP (YOUR CURRENT SOLUTION) ⭐
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            a, b = b, cost[i] + min(a, b)
        
        return min(a, b)

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only two variables
Benefits:
- Optimal space usage
- Clean and efficient implementation
- Perfect for competitive programming
- No extra array allocation

Algorithm explanation:
- a = min cost to reach step i-2
- b = min cost to reach step i-1  
- For each step i: new_cost = cost[i] + min(a, b)
- Slide window: a, b = b, new_cost
- Return min(a, b) since we can reach top from either of last two steps

APPROACH 2: BOTTOM-UP DP WITH ARRAY
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)  # dp[i] = min cost to reach step i
        
        # Base cases: can start from step 0 or 1
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # Can reach top from last step or second-to-last step
        return min(dp[n-1], dp[n-2])

Time Complexity: O(n) - single pass
Space Complexity: O(n) - store all intermediate results
Benefits:
- Easy to understand and debug
- Natural DP progression
- Good for learning DP concepts

APPROACH 3: TOP-DOWN DP WITH MEMOIZATION
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def dp(i):
            if i >= n:
                return 0  # Reached the top
            if i in memo:
                return memo[i]
            
            # Choose minimum between climbing 1 or 2 steps
            memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]
        
        # Can start from step 0 or 1
        return min(dp(0), dp(1))

Time Complexity: O(n) - each subproblem solved once
Space Complexity: O(n) - memoization + recursion stack
Benefits:
- Natural recursive thinking
- Automatic memoization
- Good for understanding the problem structure

APPROACH 4: NAIVE RECURSIVE (FOR COMPARISON)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        def dp(i):
            if i >= n:
                return 0
            
            return cost[i] + min(dp(i+1), dp(i+2))
        
        return min(dp(0), dp(1))

Time Complexity: O(2^n) - exponential, very slow
Space Complexity: O(n) - recursion depth
Issues:
- Exponential time due to overlapping subproblems
- Will timeout for large inputs
- Massive redundant calculations

STEP-BY-STEP EXAMPLE:
cost = [10, 15, 20]

Your algorithm execution:
- Initial: a=10 (cost[0]), b=15 (cost[1])
- i=2: a,b = 15, 20+min(10,15) = 15, 30
- Return min(15, 30) = 15

Optimal path: Start at index 1 (cost 15) → climb 2 steps → reach top
Total cost: 15

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

Your algorithm execution:
- a=1, b=100
- i=2: a,b = 100, 1+min(1,100) = 100, 2
- i=3: a,b = 2, 1+min(100,2) = 2, 3  
- i=4: a,b = 3, 1+min(2,3) = 3, 3
- i=5: a,b = 3, 100+min(3,3) = 3, 103
- i=6: a,b = 103, 1+min(3,103) = 103, 4
- i=7: a,b = 4, 1+min(103,4) = 4, 5
- i=8: a,b = 5, 100+min(4,5) = 5, 104  
- i=9: a,b = 104, 1+min(5,104) = 104, 6
- Return min(104, 6) = 6

PERFORMANCE COMPARISON:
- Your space-optimized: O(1) space, fastest execution
- Array DP: O(n) space, same time complexity
- Memoized recursive: O(n) space, slight overhead
- Naive recursive: O(2^n) time, extremely slow

KEY INSIGHTS:
1. This is a classic DP problem with optimal substructure
2. Can reach step i from either step i-1 or i-2, choose minimum
3. Space optimization possible since we only need previous 2 values
4. The "top" is beyond the last step, so we can reach it from last or second-to-last step

WHEN TO USE EACH APPROACH:
- Interview/LeetCode: Your space-optimized approach (shows optimization skills)
- Learning DP: Start with array-based bottom-up approach
- Recursive thinking: Use memoized top-down approach
- Never use naive recursive for large inputs

Your solution demonstrates excellent understanding of space optimization in DP problems.
It achieves optimal time complexity while minimizing space usage - perfect for competitive programming!
"""
