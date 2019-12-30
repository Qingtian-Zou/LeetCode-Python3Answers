'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

 

Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].
'''

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx=sum(nums[0:k])
        ans=mx
        for i in range(1,len(nums)-k+1):
            ans+=(nums[i-1+k]-nums[i-1])
            mx=max(ans,mx)
        return mx/k

if __name__=='__main__':
    obj=Solution()
    print(obj.findMaxAverage([0,4,0,3,2],1))