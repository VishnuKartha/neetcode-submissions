class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-2):
            target = nums[i] * -1
            l = i + 1
            r = n - 1
            while l != r:
                lr_sum = nums[l] + nums[r]
                if lr_sum == target:
                    result.add(tuple(sorted([nums[l], nums[r], nums[i]])))
                    l+=1
                elif lr_sum < target:
                    l+=1
                else:
                    r-=1
        return list(result)





       
