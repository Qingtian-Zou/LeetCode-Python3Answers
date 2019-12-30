'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in reversed(range(1,len(s)+1)):
            for ii in range(len(s)-i+1):
                sub=s[ii:ii+i]
                if sub==sub[::-1]:
                    return sub
        return None

if __name__=='__main__':
    obj=Solution()
    print(obj.longestPalindrome('cbbd'))