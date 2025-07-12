"""
Problem: 1431. Kids With the Greatest Number of Candies
Difficulty: Easy
URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

Description:
There are n kids with candies. You are given an integer array candies, where each candies[i] represents
the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.



Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]


Constraints:

n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Determine which kids can have the greatest number of candies after receiving extra candies.

        Args:
            candies: List of integers representing current candies each kid has
            extraCandies: Number of extra candies to give to one kid

        Returns:
            List[bool]: Boolean list where True means the kid can have the greatest number
        """
        result = []
        max_candies = max(candies)

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # Test case 1
    input1 = [2, 3, 5, 1, 3]  # Replace with actual input
    input2 = 3  # Replace with actual input
    expected = [True, True, True, False, True]  # Replace with expected output
    result = solution.kidsWithCandies(input1, input2)
    print(f"Test 1: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 2
    input1 = [4, 2, 1, 1, 2]  # Replace with actual input
    input2 = 1  # Replace with actual input
    expected = [True, False, False, False, False]  # Replace with expected output
    result = solution.kidsWithCandies(input1, input2)
    print(f"Test 2: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")

    # Test case 3 - Edge case
    input1 = [12, 1, 12]  # Replace with actual input
    input2 = 10  # Replace with actual input
    expected = [True, False, True]  # Replace with expected output
    result = solution.kidsWithCandies(input1, input2)
    print(f"Test 3: input1={input1}, input2={input2}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_solution()


"""
ALTERNATIVE SOLUTIONS:

# Approach 1: Current Solution (Explicit if-else)
# Time: O(n), Space: O(1)
def kidsWithCandies_v1(self, candies: List[int], extraCandies: int) -> List[bool]:
    result = []
    max_candies = max(candies)
    
    for i in range(len(candies)):
        if (candies[i] + extraCandies) >= max_candies:
            result.append(True)
        else:
            result.append(False)
    
    return result

# Approach 2: List Comprehension (Most Pythonic)
# Time: O(n), Space: O(1)
def kidsWithCandies_v2(self, candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]

# Approach 3: Using map() function
# Time: O(n), Space: O(1)
def kidsWithCandies_v3(self, candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    return list(map(lambda candy: candy + extraCandies >= max_candies, candies))

# Approach 4: Enumerate for index tracking
# Time: O(n), Space: O(1)
def kidsWithCandies_v4(self, candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    result = []
    
    for index, candy in enumerate(candies):
        result.append(candy + extraCandies >= max_candies)
    
    return result

# Approach 5: Pre-allocate result list (Best for large inputs)
# Time: O(n), Space: O(1)
def kidsWithCandies_v5(self, candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    result = [False] * len(candies)  # Pre-allocate
    
    for i in range(len(candies)):
        result[i] = candies[i] + extraCandies >= max_candies
    
    return result

# Approach 6: One-liner with max() inline
# Time: O(n²), Space: O(1) - Less efficient due to repeated max() calls
def kidsWithCandies_v6(self, candies: List[int], extraCandies: int) -> List[bool]:
    return [candy + extraCandies >= max(candies) for candy in candies]

PERFORMANCE COMPARISON:
- v1 (Current): Most readable, good for interviews
- v2 (List Comp): Most Pythonic, slightly faster
- v3 (Map): Functional style, good for functional programming fans
- v4 (Enumerate): Good when you need indices for other purposes
- v5 (Pre-allocate): Best for very large inputs, minimal memory allocation
- v6 (One-liner): Shortest but inefficient (recalculates max for each element)

RECOMMENDED: v2 (List Comprehension) for production code, v1 (Current) for learning/interviews
"""
