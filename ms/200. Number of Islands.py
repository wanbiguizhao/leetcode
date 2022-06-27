from typing import List 
class Solution:
    """
    _summary_ 深度优先遍历加递归
    1. 答题注意grid中的数据类型。
    2. 在原始矩阵上标识访问过的数据，注意恢复数据。
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        def dsp(i,j):
            directions=[[0,1],[0,-1],[-1,0],[1,0]]
            for direct in directions:
                x,y=i+direct[0],j+direct[1]
                if x>=0 and x<constM and y>=0 and y<constN and grid[x][y]=="1":
                    grid[x][y]="-1"
                    dsp(x,y)
                    
        constM=len(grid)
        constN=len(grid[0])
        ans=0
        for i in range(constM):
            for j in range(constN):
                if grid[i][j]=="1":
                    ans+=1
                    grid[i][j]=="-1"
                    dsp(i,j)
        for i in range(constM):
            for j in range(constN):
                if grid[i][j]=="-1":
                    grid[i][j]="1"# recover
        return ans 

