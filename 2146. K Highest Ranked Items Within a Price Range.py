from typing import List 
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        # BFS 
        def filter(x,y):
            return  x>= 0 and x < ROW_M and y  >=0   and y < COL_N and "{}-{}".format(x,y) not in cache_set and   grid[x][y] !=0 
        ROW_M=len(grid)
        COL_N=len(grid[0])
        ans_list=[]
        cache_set=set()
        
        priority_queue=[]
        priority_queue.append(start)
        if filter(start[0],start[1]) and pricing[0]<= grid[start[0]][start[1]] and pricing[1]>= grid[start[0]][start[1]] :
            ans_list.append(start)
        if len(ans_list)==k:
            return ans_list
        cache_set.add("{}-{}".format(start[0],start[1]))
        while priority_queue:
            tmp_list=[]
            level_ans_list=[]
            for node in priority_queue:
                for x,y in [ (node[0]-1,node[1]),
                            (node[0]+1,node[1]),
                            (node[0],node[1]-1),
                            (node[0],node[1]+1) ] :
                    if filter(x,y) :
                        cache_set.add("{}-{}".format(x,y))
                        tmp_list.append([x,y])
                        if grid[x][y]>=pricing[0] and grid[x][y]<=pricing[1]:
                            cache_set.add("{}-{}".format(x,y))
                            tmp_list.append([x,y])
                            level_ans_list.append([grid[x][y],x,y])
            level_ans_list.sort()
            for one_ans in level_ans_list:
                ans_list.append([ one_ans[-2],one_ans[-1] ])
                if len(ans_list)==k:
                    return ans_list 
            priority_queue=tmp_list 

        return ans_list 
if __name__=="__main__":
    instance=Solution()
    ans=instance.highestRankedKItems( grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3)
    print(ans)
    ans=instance.highestRankedKItems(  grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2)
    print(ans)
    ans=instance.highestRankedKItems(  [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3)
    print(ans)
    ans=instance.highestRankedKItems(  [[0,2,0]], pricing = [2,2], start = [0,1], k = 1)
    print(ans)