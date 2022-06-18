from typing import List 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            coordinate_list=[]
            coordinate_list.append((i,j))
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            while coordinate_list:
                (xo,yo)=coordinate_list.pop()
                for direct in directions:
                    x=xo+direct[0]
                    y=yo+direct[1]
                    if x >=0 and x<const_m and y>=0 and y<const_n and grid[x][y]=="1":
                        grid[x][y]="2"
                        coordinate_list.append((x,y)) 
        const_m=len(grid)
        const_n=len(grid[0])
        ans=0
        for i in range(const_m):
            for j in range(const_n):
                if grid[i][j]=="1":
                    ans+=1
                    grid[i][j]="2" # 标记
                    bfs(i,j) # 广度优先标记其他的点。
        return ans 
if __name__=="__main__":
    instance=Solution()
    instance.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]])