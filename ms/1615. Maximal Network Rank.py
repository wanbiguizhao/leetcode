import collections
from typing import List 
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # O^2 的空间和时间复杂度
        """
        1615. Maximal Network Rank

        tags:graph
        
        Runtime: 445 ms, faster than 60.66% of Python3 online submissions for Maximal Network Rank.
        Memory Usage: 15.5 MB, less than 93.53% of Python3 online submissions for Maximal Network Rank.
        """
        adjMatrix=[False ]*(n*n)# index=i*n+j 
        cityRank=[0]*n 
        for road in roads:
            cityRank[road[0]]+=1
            cityRank[road[1]]+=1 
            adjMatrix[road[0]*n+road[1]]=True
            adjMatrix[road[1]*n+road[0]]=True
        ans=0 
        for i in range(n):
            for j in range(i+1,n):
                # rank=cityRank[i]+cityRank[j]+ (-1) if adjMatrix[i*n+j] else 0 # 这个表达式会有问题
                rank=cityRank[i]+cityRank[j]
                if adjMatrix[i*n+j]:
                    rank-=1
                ans=max(ans,rank)
        return ans 
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # 使用集合做，可能使用的比较多的存储空间。
        graph = collections.defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        return max(len(graph[a]) + len(graph[b]) - (1 if b in graph[a] else 0) for a in range(n) for b in range(a + 1, n))
def testCase0(instance=Solution()):
    instance.maximalNetworkRank(2,[[0,1]])
    instance.maximalNetworkRank(2,[])
    instance.maximalNetworkRank(4,[[0,1],[1,2],[1,3],[0,2]])

def testCase0_wrong(instance=Solution()):
    # leetcode 没有通过的例子
    instance.maximalNetworkRank(8,[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]) # 53 / 82 test cases passed.

if __name__ =="__main__":
    #testCase0()
    testCase0_wrong()
    

