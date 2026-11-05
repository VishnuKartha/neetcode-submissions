class Solution:
    """
    [1,2,2,3,3,3]
    first lets get the counts of the eleements
    1:1 2:2 3:3
    Now lets create the reverse of that table (going from counts => set of elements which have that count)
    1:1 2:2 3:3
    Pop from the top of the table

    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        # 1:1, 2:2, 3:3 
        for num in nums:
            counts[num] += 1 
        freqs = [0] * len(nums)

        freq_to_nums = defaultdict(set)
        for num,count in counts.items():
            freq_to_nums[count].add(num)
        # 3: {3} 2:{2}, 1:{1}
        i = len(nums)
        res = []
        while i > 0 and k > 0:
            if len(freq_to_nums[i]) != 0:
                for num in freq_to_nums[i]:
                    if k == 0:
                        return res
                    res.append(num)
                    k-=1
            i-=1
        return res
            
        
        

        