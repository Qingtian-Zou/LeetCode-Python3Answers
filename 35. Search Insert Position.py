'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0

'''

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        while(left<right-1):
            if nums[(left+right)//2]==target:
                return (left+right)//2
            elif nums[(left+right)//2]>target:
                right=(left+right)//2
            else:
                left=(left+right)//2
        if nums[left]<target:
            return right
        else:
            return left

if __name__=="__main__":
    obj=Solution()
    print(obj.searchInsert([1,3,5,6], 5))