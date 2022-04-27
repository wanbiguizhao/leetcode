from typing import List 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def _exit(i,j,k):
            if k==len(word):
                return True
            if i<0 or i>=const_m or j <0 or j>=const_n or memory[(i,j)]:
                return False
            if word[k]!=board[i][j]:
                return False 
            memory[(i,j)]=True
            hit_flag=_exit(i+1,j,k+1) or _exit(i-1,j,k+1) or _exit(i,j+1,k+1) or _exit(i,j-1,k+1)
            if hit_flag:
                return True 
            memory[(i,j)]=False
            return False
        const_m=len(board)
        const_n=len(board[0])
        memory={}
        for i in range(const_m):
            for j in range(const_n):
                memory[(i,j)]=False
        for i in range(const_m):
            for j in range(const_n):
                if board[i][j]==word[0]:
                    memory[(i,j)]=True
                    hit_flag=_exit(i+1,j,1) or _exit(i-1,j,1) or _exit(i,j+1,1) or _exit(i,j-1,1)
                    if hit_flag:
                        return True 
                    memory[(i,j)]=False
        return False 
if __name__ == "__main__":
    instance=Solution()
    instance.exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
    instance.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")