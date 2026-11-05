class Solution:
    """
    Input: height = [0,2,0,3,1,0,1,3,2,1]
  
    m_h_to_l. =     [0,0,2,2,3,3,3,3,3,3]
    m_h_to_r =      [3,3,3,3,3,3,3,2,1,0]   
    mins     =      [0,0,2,2,3,3,3,2,1,0]
    water trapped = [0,0,2,0,2,3,2,0,0,0]
    result = 9
    
    keep track of two things; max height to the left and max_height to the right
    if the current value is less than both of them we trap water for the minimum of the values
                     0,0,2,2,3,

    max_height seen thus far:0

    Output: 9

    L = 0
    keep track of maxHeight seen thus far from left ro right

    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        m_h_to_l = [0] * n
        m_h_to_r = [0] * n
        max_height_seen = 0
        for i in range(0, n):
            m_h_to_l[i] = max_height_seen
            max_height_seen = max(max_height_seen,height[i])
        max_height_seen = 0
        for i in range(n - 1, -1, -1):
            m_h_to_r[i] = max_height_seen
            max_height_seen = max(max_height_seen,height[i])
        water_trapped = 0
        for i,h in enumerate(height):
            water_trapped += max(0, min(m_h_to_l[i], m_h_to_r[i]) - h)
        return water_trapped

        