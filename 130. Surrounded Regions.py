from doctest import FAIL_FAST
from email.base64mime import body_encode
from operator import xor
from os import rename
from time import sleep
from typing import  List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        DFS 进行判断
        """   
        def check(i,j):
            #return i>=0 and i<const_m and j>=0 and j< const_n and not helper_board[i][j] and board[i][j]=="O"  
            return i>0 and i<const_m-1 and j>0 and j< const_n-1 and not helper_board[i][j] and board[i][j]=="O" # 按理说这个判断的更少一点
        const_m=len(board)
        const_n=len(board[0])
        helper_board=[[ False  for j in range(const_n)]for i in range(const_m) ]

        # 找到所有的最终的O点
        # 依次从四周找打所有的O点，然后找到临街的O点，进行标记，这点点永远也不会变成X。
        o_point_queue=[]
        for i in range(const_m):
            if board[i][0]=="O":
                o_point_queue.append([i,0])
                helper_board[i][0]=True
            if board[i][const_n-1]=="O":
                o_point_queue.append([i,const_n-1])
                helper_board[i][const_n-1]=True 
        for j in range(const_n):
            # row 0, m
            if board[0][j]=="O":
                helper_board[0][j]=True
                o_point_queue.append([0,j])
            if board[const_m-1][j]=="O":
                helper_board[const_m-1][j]=True
                o_point_queue.append([const_m-1,j])
        while  o_point_queue:
            [x,y]=o_point_queue.pop(0)
            if check(x-1,y):
                o_point_queue.append([x-1,y])
                helper_board[x-1][y]=True
            if check(x+1,y):
                o_point_queue.append([x+1,y])
                helper_board[x+1][y]=True
            if check(x,y-1):
                o_point_queue.append([x,y-1])
                helper_board[x][y-1]=True
            if check(x,y+1):
                o_point_queue.append([x,y+1])
                helper_board[x][y+1]=True 

        for i in range(const_m):
            for j in range(const_n):
                if not helper_board[i][j] and board[i][j]=="O":
                    board[i][j]="X"
        return 
        
                 
if __name__ == "__main__":
    instance=Solution()
    instance.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
    instance.solve([["X"]])