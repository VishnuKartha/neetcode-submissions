"""
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution should run in 
O(log(m+n)) time.

1. Suppose we have two sorted arrays
n = len(nums1) + len(nums2)
nums1 = [1,2,3] nums2 = [4,5]
We need to find the median of the combined array
combined = [1,2,3,4,5] 3 i s the median
if n % 2 == 1 the median is the single middle number
if we have nums1 = [1,2,3] nums = [4,5,6]
The median of the combined array
combined = [1,2,3,4,5,6] median = 3 + 4 //2
if n % 2 == 0 the median is the average of the two middle numbers

nums1 = [9] nums1 = [1,2]

median = middle of [1,2,9] = 2
lets try to split the array into two halfs AL, 
such that AL = [1,2] AR = 3. The left side has numbers <= the median the right side has numbers > median
n = 2 + 1 
n + 1 // 2 = 2
The left side we can see has the smallest 
n+1 // 2 elements
If we split an array into these halves the median is trivial it is just max(AL)
if n % 2 == 0:
    AL = [1,2] AR = [3,4]
    its max(AL) + min (AR) // 2

nums1 = [1,2,3] nums2 = [1,2]

Let AL = the n + 1 // 2 element long smallest elements of{nusm1,nums2} which contains {nums1[:i], nums2[:j]}

Our goal is to find the first number i such that
{nums1[:i], nums2[:j]} is the smallest k elements.

which means finding the first index i such that
nums2[j-1] <= nums2[i], 
[1,1,2,3] [5,6] k = 4 
[1,1,2,3] [5,6] k = 4 
[1,1,5,6] = AL
[2,3] = AR
i = 2 j = 2
[1,1] [5,6]

if = k = 3 and we no elements in nums2 
lower bound of i = max(0, len(nums2) - k)
upper bound of i  = min(len(nums1), k)

n = len(nums1) + len(nums2)
def split(nums1,nums2):
    k = n + 1 // 2
    lo = max(0, len(nums2) - k)
    hi = min(len(nums1), k)
    while lo < hi:
        i = lo + hi // 2
        j = k - i
        if nums[j - 1] <= nums[i]:
            hi = mid
        else: 
            lo = mid + 1
    return lo, k - lo
i,j = split(nums1,nums2)
maxAL = -inf
minAR = inf
if i > 0:
    maxAL = max(maxAL, nums1[i-1])
if j > 0:
    maxAL = max(maxAL, nums2[j-1])
if i < len(nums1):
    minAR = min(minAR,nums1[i])
if j < len(nums2):
    minAR = min(minAR,nums2[j])
if n % 2 == 1:
    return maxAL
else return (minAR + maxAL) / 2


if n % 2 == 0:
    if i == 0: nums1Val = 
    return max(nums1[lo], nun)










k = n + 1 // 3
j = k - i
[0,0,0] [1,2]
say i = 2
K = 1
AL = [0,0] [1]
Are these the smallest elements in the array no
so lets get rid of the t
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        def split(nums1,nums2):
            k = (n + 1) // 2
            # k = 3
            # [1,2,3,4] [8]
            # lo = 2

            #[1,2,3] [5]
            # Keep swapping the next element of i
            # with the biggest element from j
            # as long as the next element of i is
            # <= the biggest element from j
            # I agree that seems safe. 
            # Why is that sufficient? 
            #[5] [1,2,3] k = 2 lo = (0)hi = 1 
            # mid = 0 + 1 // 2= 0 
            #
            lo = max(0, k - len(nums2))
            hi = min(len(nums1), k)
            while lo < hi:
                i = (lo + hi) // 2
                j = k - i
                if nums2[j - 1] <= nums1[i]:
                    hi = i
                else: 
                    lo = i + 1
            return lo, k - lo
        i,j = split(nums1,nums2)
        maxAL = float("-inf")
        minAR = float("inf")
        if i > 0:
            maxAL = max(maxAL, nums1[i-1])
        if j > 0:
            maxAL = max(maxAL, nums2[j-1])
        if i < len(nums1):
            minAR = min(minAR,nums1[i])
        if j < len(nums2):
            minAR = min(minAR,nums2[j])
        if n % 2 == 1:
            return maxAL
        else:
            return (minAR + maxAL) / 2
            