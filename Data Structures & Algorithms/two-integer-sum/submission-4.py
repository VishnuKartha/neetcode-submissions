class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_before = {}

        for i,num in enumerate(nums):
            curr_target = target - num
            if curr_target in seen_before:
                match_idx = seen_before[curr_target]
                return [match_idx,i]
            seen_before[num] = i

        return [-1, -1]
            

        