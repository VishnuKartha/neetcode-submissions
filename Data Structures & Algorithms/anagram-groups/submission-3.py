class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_counts_str(word):
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord('a')] += 1
            res_str = ""
            for i,count in enumerate(counts):
                char = chr(ord('a') + i )
                res_str += char * count 
            return res_str
                
        all_count_str = [get_counts_str(word) for word in strs]
        anagram_groups = {}
        for i,count_str in enumerate(all_count_str):
            prev_val = anagram_groups.get(count_str,[])
            prev_val.append(strs[i])
            anagram_groups[count_str] = prev_val
        return list(anagram_groups.values())







        