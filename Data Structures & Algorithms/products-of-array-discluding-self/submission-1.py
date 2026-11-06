"""

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

idea 2: 
prefix multiplications and postfix products

first go through array l to r with prefixes multiplications

[1,1,2,8]

now go through array r to l with postfix multiplications

[48,24,6,1]

now for each element u multiply prefix * postfix

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1] * len(nums)
        postfix_mul = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_mul[i] = (prefix_mul[i-1] * nums[i-1])
        for i in range(len(nums) - 2, -1,-1):
            postfix_mul[i] = (postfix_mul[i+1] * nums[i+1])
        res = []
        for i in range(len(nums)):
            res.append(prefix_mul[i] * postfix_mul[i])
        return res
        


                 

        