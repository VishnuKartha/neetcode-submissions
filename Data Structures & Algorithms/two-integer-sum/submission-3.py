class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}
        for i,num in enumerate(nums):
            if target - num in nums_seen:
                return [nums_seen[target - num], i]
            else:
                nums_seen[num] = i
        return None




        