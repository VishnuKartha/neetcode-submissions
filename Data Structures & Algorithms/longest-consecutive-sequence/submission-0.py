"""
Input: nums = [2,20,4,10,3,4,5]
               i   



answer [2,3,4,5] 

[2,3,4,4,5,10,20]

idea sort the array.
then greedily pick the consecutive sequenc
o(nlog n)

throw all the elements into a hashset()

iterate through elements of the array as the (root) of the hashset lookups

[2,3,4,4,5,10,20]

{2,3,4,5,10,20}

whats the longest consecutive sequence starting with you get 4 the answer


Input: nums = [0,3,2,5,4,6,1,1]

hashet 
{0,1,2,3,4,5,6}

idea is go up and down the hashset to explore and mark numbers as travelled

Output: 4
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set()
        for num in nums:
            all_nums.add(num)
        seen = set()
        res = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                curr_len = 1
                temp = num+1
                while temp in all_nums:
                    seen.add(temp)
                    curr_len += 1
                    temp+=1
                temp = num - 1
                while temp in all_nums:
                    seen.add(temp)
                    curr_len +=1
                    temp -=1
                res = max(res,curr_len)
        return res
                




        