class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        L = 0
        R = len(height) - 1
        maxL = 0
        maxR = 0
        while L <= R:
            waterTrapped = 0
            if maxL < maxR:
                # look at the L index
                waterTrapped = max(maxL - height[L],0)
                maxL = max(height[L], maxL)
                L+=1
            else:
                waterTrapped = max(maxR - height[R],0)
                maxR = max(height[R], maxR)
                R-=1
            res += waterTrapped
        return res





        