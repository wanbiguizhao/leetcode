from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Q : can same letter cell be used more the once ?
        # Q: m is the length of Row  and n is the length of Col?
        # solution
        # i will use DFS as the solution of this question and pay attention for bounds in every step 
        # first , i will construct a directions array which help program choice forward direction and pay attention for bounds in every step 
        # second, a visted matrix will be constucted for  used letter 
        def dfs(x,y,pos):
            if pos==len(word):
                self.find=True 
                return 
            if self.find or x<0 or x>=constRowNum or y<0 or y>=constColNum or visited[(x,y)]:
                return 
            if board[x][y]==word[pos]:
                visited[(x,y)]=True 
                for direct in directions:
                    dx,dy=direct[0],direct[1]
                    xn,yn=x+dx,y+dy
                    dfs(xn,yn,pos+1) 
                visited[(x,y)]=False

        constRowNum=len(board)
        constColNum=len(board[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited={}
        self.find=False
        for i in range(constRowNum):
            for j in range(constColNum):
                visited[(i,j)]=False 
        for i in range(constRowNum):
            for j in range(constColNum):
                if self.find:
                    break
                dfs(i,j,0)
            if self.find:
                break
        return self.find


        
def testCase0(instance=Solution()):
    res=instance.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
    print(res,True)
    res=instance.exist(board = [["D","C"],["A","B"]], word = "ABCD")
    print(res,True)
def testCase0_wrong(instance=Solution()):
    # leetcode 没有通过的例子
    pass 
if __name__ =="__main__":
    testCase0()
    testCase0_wrong()
    


            