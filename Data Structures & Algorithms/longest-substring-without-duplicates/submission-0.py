"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
log(n)

Idea we make the longest substring starting at s[L]. If we see a repeat we must increase 

Input: s = "zxyzxyz"
            L
             R

subset is s[L:R]
{x,y,z}
substring being looked at is s[L:R]
Output: 3


"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        L = 0
        R = 0
        n = len(s)
        curr_set = set()
        while(R < n):
            while s[R] in curr_set:
                curr_set.remove(s[L])
                L+=1
            curr_set.add(s[R])
            res = max(len(curr_set),res)
            R+=1
        return res

            
        