"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3
                 l      r
                 1 + 4 > 3 we need the sum to be smaller so r-=1
                 1 + 3 > 3 we need the sum to be smaller so r -=1
                 1 + 2 = 3 solution


Output: [1,2]
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if target == numbers[l] + numbers[r]:
                return [l+1,r+1]
            elif target > numbers[l] + numbers[r]:
                l+=1
            else:
                r-=1
        return [-1,-1]
        