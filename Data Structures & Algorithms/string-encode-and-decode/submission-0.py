class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for curr in strs:
            res += str(len(curr))+ "#" + curr
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            string_len = int(s[i:j])
            i = j + 1 + string_len
            res.append(s[j+1: i])
        return res
            


