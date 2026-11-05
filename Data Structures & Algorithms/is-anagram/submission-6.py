class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_map = defaultdict(int)

        for ch in s:
            s_map[ch] +=1

        
        for ch in t:
            s_map[ch] -=1

        for k,v in s_map.items():
            if v != 0:
                return False
                
        return True


        # idea for each string make a set of tuples which contains the counts of each
        # character then say its true if the counts match

        # racecar
        # i
        # {r: 1}
        # {j: a}

        