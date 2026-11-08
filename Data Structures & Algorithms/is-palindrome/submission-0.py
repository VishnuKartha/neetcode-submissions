"""
Input: s = "Was it a car or a cat I saw?"
            i                          j
            lets make the string to lower case and remove spaces
            wasitacaroracatisaw
                i               
                j

Output: true
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) -1
        l = 0
        while l <= r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
            


        