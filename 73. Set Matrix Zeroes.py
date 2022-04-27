from typing import List 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        之前做过，发现（i,j）为零设置[0,j],[i,0]为零，然后寻找所有的[0,x]把所有的x列设置为0，同理这是所有的[y,0]设置所有的y为0.
        主要考察观察能力观察
        """
        const_m=len(matrix)
        const_n=len(matrix[0])
        first_col_zero=not all(matrix[i][0] for i in range(const_m) )
        
        first_row_zero=not all([ matrix[0][j] for j in range(const_n) ] ) 
        
        for i in range(const_m):
            for j in range(const_n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,const_m):
            if matrix[i][0]==0:
                for j in range(const_n):
                    matrix[i][j]=0
        for j in range(1,const_n):
            if matrix[0][j]==0:
                for i in range(const_m):
                    matrix[i][j]=0
        if first_col_zero : # 注意需要做一些保留
            for i in range(const_m):
                matrix[i][0]=0
        if first_row_zero:
            for j in range(const_n):
                matrix[0][j]=0
        return 
            
if __name__ == "__main__":
    instance=Solution()
    # instance.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
    # instance.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
    instance.setZeroes([[1,0,3]])

        
        