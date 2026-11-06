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

idea 1: multiply everything together and count number of 0s

1 * 2 * 4 * 6 

0 : 0s

now for each value go and divide by the curr. if there are 2+ 0's its 0s throughout. if its 1 zero its zeros throughout except for the position
of the zero. so you only have to calculate the multiplcation of that one position


Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        for num in nums:
            if num == 0:
                num_zeros +=1
        if num_zeros >= 2:
            return [0 for i in range(len(nums))]
        if num_zeros == 1:
            product = 1
            zero_idx = -1
            for i,num in enumerate(nums):
                if num == 0:
                    zero_idx = i
                else:
                    product *= num
            res = [0 for i in range(len(nums))]
            res[zero_idx] = product
            return res
        else:
            product = 1
            res = []
            for num in nums:
                product *= num
            for num in nums:
                res.append(product // num)
            return res
            
                 

        