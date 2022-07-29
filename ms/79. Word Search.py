from typing import List
class Solution:
    # 使用set数据结构，可以降低内存使用，但是加入和减少元素特别耗费时间。
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
        #visited={}
        visited=set()
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
            if self.find or x<0 or x>=constRowNum or y<0 or y>=constColNum or visited[x][y]:
                return 
            if board[x][y]==word[pos]:
                visited[x][y]=True 
                for direct in directions:
                    dx,dy=direct[0],direct[1]
                    xn,yn=x+dx,y+dy
                    dfs(xn,yn,pos+1) 
                visited[x][y]=False

        constRowNum=len(board)
        constColNum=len(board[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[False for _ in range(constColNum)] for _ in range(constRowNum)]# 学习的初始化数组的地方。
        # 使用数组构造visited 比使用字典快。
        self.find=False

        for i in range(constRowNum):
            for j in range(constColNum):
                if self.find:
                    break
                dfs(i,j,0)
            if self.find:
                break
        return self.find
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 最高效的方法
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
            if self.find or x<0 or x>=constRowNum or y<0 or y>=constColNum or visited[x][y]:
                return 
            if board[x][y]==word[pos]:
                visited[x][y]=True 
                dfs(x+1,y,pos+1)
                dfs(x-1,y,pos+1)
                dfs(x,y+1,pos+1)
                dfs(x,y-1,pos+1)
                # for direct in directions:
                #     dx,dy=direct[0],direct[1]
                #     xn,yn=x+dx,y+dy
                #     dfs(xn,yn,pos+1)
                #     if self.find:
                #         break
                visited[x][y]=False

        constRowNum=len(board)
        constColNum=len(board[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[False for _ in range(constColNum)] for _ in range(constRowNum)]
        self.find=False

        for i in range(constRowNum):
            for j in range(constColNum):
                
                dfs(i,j,0)
                if self.find:
                    break
            if self.find:
                break
        return self.find
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
            if self.find or x<0 or x>=constRowNum or y<0 or y>=constColNum or visited[x][y]:
                return 
            if board[x][y]==word[pos]:
                visited[x][y]=True 
                dfs(x+1,y,pos+1)
                dfs(x-1,y,pos+1)
                dfs(x,y+1,pos+1)
                dfs(x,y-1,pos+1)
                # for direct in directions:
                #     dx,dy=direct[0],direct[1]
                #     xn,yn=x+dx,y+dy
                #     dfs(xn,yn,pos+1)
                #     if self.find:
                #         break
                visited[x][y]=False

        constRowNum=len(board)
        constColNum=len(board[0])
        visited=[[False for _ in range(constColNum)] for _ in range(constRowNum)]
        self.find=False

        for i in range(constRowNum):
            for j in range(constColNum):
                dfs(i,j,0)
                if self.find: # 优雅的结束程序运行的方式：Elegant way to end program execution
                    return True
        return False

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
    


            