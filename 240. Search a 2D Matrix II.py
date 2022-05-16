from typing import List 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 尝试二分查找结果
        const_m=len(matrix)-1
        const_n=len(matrix[0])-1
        i,j=0,0
        left,bottom,m,n=0,0,const_m,const_n
        while left<=n and bottom<=m:
            if matrix[bottom][n]>target:
                n-=1
            elif matrix[bottom][n]<target:
                bottom+=1
            else:
                return True 
            if matrix[m][left]>target:
                m-=1
            elif matrix[m][left]<target:
                left+=1
            else:
                return True 
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 尝试二分查找结果
        # 更干净的做法，找右边上角的元素
        ROW_LEN=len(matrix)
        COL_LEN=len(matrix[0])
        i=0
        j=COL_LEN-1
        while i<ROW_LEN and j>=0:
            if target==matrix[i][j]:
                return True
            elif target>matrix[i][j]:
                i=i+1
            else:
                j=j-1
        return False