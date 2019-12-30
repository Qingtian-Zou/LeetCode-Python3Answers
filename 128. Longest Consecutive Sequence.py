'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype max_combo: int
        """
        if(nums==[]):
            return 0
        nums.sort()
        temp=1
        max_combo=1
        for index in range(len(nums)-1):
            if nums[index]+1==nums[index+1]:
                temp+=1
            elif nums[index]==nums[index+1]:
                continue
            else:
                temp=1
            if max_combo<temp:
                max_combo=temp
        return max_combo
        
if __name__ == "__main__":
    A=[0,0]
    s=Solution()
    print(s.longestConsecutive(A))