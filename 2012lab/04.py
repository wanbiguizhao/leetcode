
from typing import List
from collections import Counter,defaultdict
import functools
class Solution:
    # tag: 图 暴力搜索  二进制
    def run(self, m:int,n:int,edges:List[List[int]]) -> int:
        # m节点个数
        # 边长个数
        # 根据图中的示例答案，节点的index从1开始。
        ans=0
        for i in range(2**m):
            # 一些二进制的代码
            bin_i=bin(i)[2:].rjust(m,'0')# 题眼
            pass_flag=True
            for edge in edges:
                a_node,b_node=edge[0]-1,edge[1]-1
                if bin_i[a_node]==bin_i[b_node] and bin_i[a_node]=='1':
                    pass_flag=False
                    break
            if pass_flag:
                ans+=1
        return ans
s=Solution()
print(
    s.run(4,0,[])
)
print(
    s.run(4,1,[[1,4]])
)
print(
    s.run(4,2,[[1,4],[1,3]])
)
print(
    s.run(4,3,[[1,4],[1,3],[1,2]])
)
print(
    s.run(4,4,[[1,4],[1,3],[1,2],[2,4]])
)