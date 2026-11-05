class Solution:
    """
    Input: height = [0,2,0,3,1,0,1,3,2,1]
                     l                 r
    l = 0
    r = 0
    prefix_max(l) = max value seen left of height[l]
    prefix_max(r) = max value seen left of height[r]
    postfix_max(r) = max value seen right of height[r]
    postfix_max(l) = vax value seen right of height[l]
    water_trapped(i) = the water trapped at index i
    if prefix_max(l) <= postfix_max(r):
        water_trapped(l) =  min(postfix_max(l),prefix_max(l)) - height[l]
        Since we know the following,
        postfix_max(l) >= postfix_max(r)  // since r > l
        and postfix_max(r) >= prefix_max(l) # if statement condition
        this reduces to 
        water_trapped(l) =  prefix_max(l) - height[l]
    else # postfix_max(r) < prefix_max(l):
        water_trapped(r) =  min(postfix_max(r),prefix_max(r)) - height[r]
        Since we know the following,
        prefix_max(r) >= prefix_max(l) (since l is before r)
        and prefix_max(l) > postfix_max(r) # if statement condition
        This reduces to 
        water_trapped(r) = postfix_max(r) - height[r]

         



  

    
    keep track of two things; max height to the left and max_height to the right
    if the current value is less than both of them we trap water for the minimum of the values
                     0,0,2,2,3,

    max_height seen thus far:0

    O

    """
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        prefix_max_l = 0
        postfix_max_r = 0
        res = 0
        while (l <= r):
            if prefix_max_l <= postfix_max_r:
                res += max(prefix_max_l - height[l], 0)
                prefix_max_l = max(height[l], prefix_max_l)
                l+=1
            else:
                res += max(postfix_max_r - height[r], 0)
                postfix_max_r = max(height[r], postfix_max_r)
                r-=1 
        return res



        