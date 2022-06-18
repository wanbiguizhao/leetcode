from typing import List 
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_neighbors_count(i,j):
            directions=[
                (0,1),
                (1,0),
                (1,1),
                (0,-1),
                (-1,0),
                (-1,-1),
                (1,-1),
                (-1,1)
            ]
            count=0
            for direct in directions:
                x,y=i+direct[0],j+direct[1]
                if x>=0 and x<const_x and y>=0 and y<const_y and board[x][y]%2==1:
                    count+=1
            return count
        const_x=len(board)
        const_y=len(board[0])
        for ri in range(const_x):
            for cj in range(const_y):
                lives_count=get_neighbors_count(ri,cj)
                if board[ri][cj]==0 and lives_count==3:
                    board[ri][cj]+=2
                elif  board[ri][cj]==1 and lives_count<2:
                    board[ri][cj]+=2 
                elif board[ri][cj]==1 and lives_count==2 or lives_count==3:
                    pass
                elif board[ri][cj]==1 and lives_count>3:
                    board[ri][cj]+=2 
        for ri in range(const_x):
            for cj in range(const_y):
                if board[ri][cj]==2:
                    board[ri][cj]=1
                elif board[ri][cj]==3:
                    board[ri][cj]=0


if __name__ =="__main__":
    instance=Solution()
    instance.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])


