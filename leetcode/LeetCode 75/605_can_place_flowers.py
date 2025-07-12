"""
Problem: 605. Can Place Flowers
Difficulty: Easy
URL: https://leetcode.com/problems/can-place-flowers/submissions/1695390892/?envType=study-plan-v2&envId=leetcode-75

Description:
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Check if n flowers can be planted without violating adjacency rules.

        Uses greedy approach: try to plant flowers from left to right.

        Args:
            flowerbed: List of 0s and 1s representing empty/occupied plots
            n: Number of new flowers to plant

        Returns:
            bool: True if n flowers can be planted, False otherwise
        """
        count = 0
        i = 0

        while i < len(flowerbed):
            # Check if current position is empty and neighbors are empty (or don't exist)
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):

                flowerbed[i] = 1  # Plant flower
                count += 1

                if count >= n:  # Early termination optimization
                    return True
            i += 1

        return count >= n

    def canPlaceFlowers_mathematical(self, flowerbed: List[int], n: int) -> bool:
        """
        Mathematical approach (YOUR ORIGINAL) - Works as necessary condition only.

        ❌ ISSUE: This gives False positives for cases like [0,1,0] where
        theoretical max=2 but actual available spots=0 due to adjacency.
        """
        half_length = len(flowerbed) // 2
        remainder = len(flowerbed) % 2
        max_possible_flowers = half_length + remainder
        existing_flowers = flowerbed.count(1)
        return existing_flowers + n <= max_possible_flowers


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = [1, 0, 0, 0, 1]  # Replace with actual input
    input2 = 1  # Replace with actual input
    expected = True  # Replace with expected output
    result = solution.canPlaceFlowers(input1, input2)
    print(f"Test 1: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = [1, 0, 0, 0, 1]  # Replace with actual input
    input2 = 2  # Replace with actual input
    expected = False  # Replace with expected output
    result = solution.canPlaceFlowers(input1, input2)
    print(f"Test 2: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3 - Edge case: all zeros
    input1 = [0, 0, 0, 0, 0]
    input2 = 3
    expected = True  # Can place at positions 0, 2, 4
    result = solution.canPlaceFlowers(input1, input2)
    print(f"Test 3: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 4 - Edge case: single empty plot
    input1 = [0]
    input2 = 1
    expected = True
    result = solution.canPlaceFlowers(input1, input2)
    print(f"Test 4: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 5 - Edge case: alternating pattern
    input1 = [0, 0, 1, 0, 0]
    input2 = 1
    expected = True  # Can place at position 0 or 4
    result = solution.canPlaceFlowers(input1, input2)
    print(f"Test 5: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 6 - FAILING CASE: Mathematical approach fails here
    input1 = [0, 1, 0]
    input2 = 1
    expected = False  # Cannot place anywhere due to adjacency
    result = solution.canPlaceFlowers(input1, input2)
    print(f"Test 6: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")
    if result != expected:
        print("❌ Mathematical approach fails: thinks max=2, but actual available=0")


if __name__ == "__main__":
    test_solution()


"""
ISSUE WITH MATHEMATICAL APPROACH:

Your original mathematical approach was clever but had a flaw:

MATHEMATICAL APPROACH (YOUR ORIGINAL):
- Calculates theoretical maximum: ceil(length/2)
- Checks if existing + n <= max_possible
- ❌ FAILS on [0,1,0], n=1:
  * Length=3, max_possible=2, existing=1, n=1
  * Check: 1+1 <= 2 ✓ (says True)
  * Reality: Cannot place anywhere due to adjacency ❌

WHY IT FAILS:
- Works as NECESSARY condition (if this fails, definitely impossible)
- NOT SUFFICIENT condition (passing this doesn't guarantee success)
- Doesn't consider actual adjacency constraints

CORRECTED APPROACHES:

# Approach 1: Greedy Simulation (CORRECT - Current Implementation)
# Time: O(n), Space: O(1)
def canPlaceFlowers_v1(self, flowerbed: List[int], n: int) -> bool:
    count = 0
    i = 0
    
    while i < len(flowerbed):
        if (flowerbed[i] == 0 and 
            (i == 0 or flowerbed[i-1] == 0) and 
            (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
            
            flowerbed[i] = 1  # Plant flower
            count += 1
            if count >= n:
                return True
        i += 1
    
    return count >= n

# Approach 2: Mathematical (Your Original - FLAWED)
# ❌ Use only as optimization for early rejection
def canPlaceFlowers_mathematical_flawed(self, flowerbed: List[int], n: int) -> bool:
    max_possible = (len(flowerbed) + 1) // 2
    existing = flowerbed.count(1)
    return existing + n <= max_possible  # Not sufficient!

# Approach 3: Hybrid (Mathematical + Greedy)
# Use mathematical as early filter, then greedy for actual check
def canPlaceFlowers_hybrid(self, flowerbed: List[int], n: int) -> bool:
    # Quick rejection using mathematical approach
    max_possible = (len(flowerbed) + 1) // 2
    existing = flowerbed.count(1)
    if existing + n > max_possible:
        return False  # Definitely impossible
    
    # Now do actual greedy simulation
    return self.canPlaceFlowers_v1(flowerbed, n)

LESSON LEARNED:
- Mathematical optimizations are great for early rejection
- Always validate with actual constraints (adjacency rules)
- Your mathematical insight was valuable - just needed the greedy follow-up!

FINAL RECOMMENDATION: Use the greedy approach (v1) - it's the standard LeetCode solution.
"""
