"""
["act","pots","tops","cat","stop","hat"]

anagram has the same exact character but the order is different, so why dont we have a key
of the sorted version of the strings or the counts of the strings and use that as a key of 
a map which groups the characters

lets start with the sort of the strings

{"act":["act","cat"], "opts":["tops","stop'],"aht":["hat"]}
["act","pots","tops","cat","stop","hat"]

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] +=1
            anagramDict[tuple(count)].append(s)
        return list(anagramDict.values())

            

        