from typing import List 
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 计算每个节点的入度值
        # 把每个入度为零的节点放到zero_list
        # 然后一层一层的移出
        # 最后剩余节点，是否为零0 为零true。
        # 0<-1 完成0 必须完成1  
        indegree_dict={x:0 for x in range(numCourses)}
        outdegree_info_dict={x:[] for x in (numCourses) }
        # 记录每个节点的入度的值
        # 记录每个节点出度关联的节点。
        for req in prerequisites:
            indegree_dict[req[1]]+=1
            outdegree_info_dict[ req[1] ].append( req[0] )# 可以告知req[0] 依赖的req[1] 已经完成了
        zero_list=[]
        for node,indegree in indegree_dict.items():
            if indegree==0:
                zero_list.append(node )

        

