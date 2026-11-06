""" 
 Input: nums = [1,2,2,3,3,3], k = 2

frequency = {3: [3], 2: [2], 1:[1]}
frequency.sort()
pop first 1 
[3]
frequency = {2: [2], 1:[1]}

pop second {1: [1]}
[2]
frequency.sort()




 Output: [2,3]
 """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] +=1
        # counts [val : count]
        freqs = defaultdict(list)
        for num, count in counts.items():
            freqs[count].append(num)
        
        freqs = dict(sorted(freqs.items(), reverse=True))
        res = []
        for count, vals in freqs.items():
            for val in vals:
                res.append(val)
                if len(res) == k:
                    return res
        return -1 

            
        
        