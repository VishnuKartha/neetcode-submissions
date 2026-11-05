# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        # I[5,2,3,6,2]
        # 1[5,2,3,6,2]
        # 2[2,5,3,6,2]
        # 3[2,3,5,6,2]
        # 4[2,3,5,6,2]
        # 5[2,2,3,5,6]
        n = len(pairs)
        if n == 0: return []
        result.append(pairs)
        for i in range(1, n):
            new_res = []
            has_added = False
            for j in range(0, i):
                prev = result[-1]
                if not has_added and pairs[i].key < prev[j].key:
                    new_res.append(pairs[i])
                    has_added = True
                new_res.append(prev[j])
            if not has_added:
                new_res.append(pairs[i])
            for k in range(i+1,n):
                new_res.append(pairs[k])
            result.append(new_res)
        return result;


        