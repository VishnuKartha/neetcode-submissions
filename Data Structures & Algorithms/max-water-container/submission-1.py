class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        L = 0
        R = len(heights) - 1
        while L < R:
            if heights[L] < heights[R]:
                curr_water = (R-L) * heights[L]
                L+=1
            else:
                curr_water = (R-L) * heights[R]
                R -= 1
            max_area = max(curr_water, max_area)
        return max_area
        