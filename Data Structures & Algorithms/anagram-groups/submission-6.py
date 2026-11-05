class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_counts_str(word):
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord('a')] += 1
            res_str = tuple(counts)
            return res_str
                
        all_count_str = [get_counts_str(word) for word in strs]
        anagram_groups = defaultdict(list)
        for i,count_str in enumerate(all_count_str):
            anagram_groups[count_str].append(strs[i])

        return list(anagram_groups.values())







        