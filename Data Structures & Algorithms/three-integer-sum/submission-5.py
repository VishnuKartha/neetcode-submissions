"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

nums.sort()
[-1,0,1,2,-1,-4]
[-1,-1,2]
[-4,-1,-1,0,1,2] target = 4 
     i
        j           
              k
j (i + 1 to k -1)

[-4 + -1 + 2 = -3]
[-1 + -1 + 2 = 0] *
-1 + 0  + 2 = 1

res = set()

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    l+=1
        return res

        