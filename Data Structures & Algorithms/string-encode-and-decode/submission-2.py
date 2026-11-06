"""
Idea prefix each of the word in the string with its length
search the places where o is used

5|Hello5|World

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "|"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr_len = 0
        i = 0
        while i < len(s):
            j = i
            while s[j] != "|":
                j += 1
            curr_len = int(s[i:j])
            start_idx = j+1
            end_idx = start_idx + curr_len
            res.append(s[start_idx:end_idx])
            i = end_idx
        return res
