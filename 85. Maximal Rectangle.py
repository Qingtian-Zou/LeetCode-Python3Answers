'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

'''

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_rect=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                mat=[]
                if matrix[i][j]=='1':
                    ii=i
                    jj=j
                    while(jj<len(matrix[i]) and matrix[ii][jj]=='1'):
                        jj+=1
                    mat.append(jj-j)
                    while(jj!=j):
                        while(ii<len(matrix) and '0' not in matrix[ii][j:jj]):
                            ii+=1
                        mat.append((ii-i)*(jj-j))
                        try:
                            jj=j+matrix[ii][j:jj].index('0')
                        except ValueError as identifier:
                            break
                        except IndexError as identifier:
                            break
                    if max_rect<max(mat):
                        max_rect=max(mat)
        return max_rect

if __name__=='__main__':
    obj=Solution()
    tmp=[["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]
    print(obj.maximalRectangle(tmp))
