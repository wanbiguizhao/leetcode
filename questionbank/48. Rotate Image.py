from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 沿着对角线[0,0][n,n]这条线 对折，然后再沿着中间的线对折。
        const_n=len(matrix)
        for ri in range(const_n):
            for cj in range(ri+1,const_n):
                # 上三角折一下
                matrix[ri][cj],matrix[cj][ri]=matrix[cj][ri],matrix[ri][cj]
        # 沿着竖直方向进行对折
        for ri in range(const_n):
            for cj in range(0,const_n//2):
                matrix[ri][cj],matrix[ri][const_n- cj-1]=matrix[ri][const_n- cj-1],matrix[ri][cj]
        return matrix 


        