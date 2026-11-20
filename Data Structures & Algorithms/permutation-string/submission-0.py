"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 10000






    
    

s = set()
  l e c a b e e
L 0
R 0

s  




"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        a1 = [0] * 26
        a2 = [0] * 26
        for ch in s1:
            a1[ord(ch) - ord("a")] +=1

        def is_permuation(a1, a2):
            for i in range(len(a1)):
                if(a1[i] != a2[i]):
                    return False
            return True

        for R in range(len(s1)):
            a2[ord(s2[R]) - ord("a")] +=1
      
        "  l e c a b e e"
        "  L     R    "
        for R in range(len(s1), len(s2) + 1):
            L = R - len(s1)
            if is_permuation(a1,a2):
                return True
            else:
                a2[ord(s2[L]) - ord("a")] -=1
                if R != len(s2):
                    a2[ord(s2[R]) - ord("a")] +=1
                R+=1
        return False
        