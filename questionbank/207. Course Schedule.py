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
        outdegree_info_dict={x:[] for x in range(numCourses) }
        # 记录每个节点的入度的值
        # 记录每个节点出度关联的节点。
        for req in prerequisites:
            indegree_dict[req[0]]+=1
            outdegree_info_dict[ req[1] ].append( req[0] )# 可以告知req[0] 依赖的req[1] 已经完成了
        zero_list=[]
        ans=numCourses
        for node,indegree in indegree_dict.items():
            if indegree==0:
                zero_list.append(node )
               
        while zero_list:
            x_node=zero_list.pop(0)
            ans-=1
            for z_node in outdegree_info_dict[x_node]:
                indegree_dict[z_node]-=1
                if indegree_dict[z_node]==0:
                    zero_list.append(z_node)
        return ans==0


if __name__=="__main__":
    instance=Solution()
    instance.canFinish(2,[1,0])

