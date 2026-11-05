class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
          
          |       |
          |       |   |
          |   |   |   |
          |   | | |   |
          |   | | | | |
          | | | | | | |
        | | | | | | | |
                  L
                  R

        the formula to calculate the amount of water in a tank
        is (R - L) * min(R,L)
        Since we want the max we should greedily get rid of the smaller L or R on each 
        side 


        """

        l = 0
        r = len(heights) - 1
        max_water = 0
        while l != r:
            curr_water = (r - l) * min(heights[l], heights[r]) 
            max_water = max(curr_water, max_water)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return max_water

        