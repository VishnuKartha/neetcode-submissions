class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_counts_str(word):
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord('a')] += 1
            return tuple(counts)
                
        anagram_groups = defaultdict(list)
        for s in strs: 
            anagram_groups[get_counts_str(s)].append(s)

        return list(anagram_groups.values())







        