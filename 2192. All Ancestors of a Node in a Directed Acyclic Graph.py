from collections import defaultdict
from typing import List 
class Solution:
    def getAncestors2(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 存在重复遍历某些节点的情况。
    
        in_degree_cache=defaultdict(set)
        for edge in edges:
            from_node,to_node=edge
            in_degree_cache[to_node].add(from_node)
        ans=[]
        for node_id in range(n):
            node_ans=set()
            node_list=set([node_id])
            while node_list:
                t_node_set=set()
                for to_node in node_list:
                    t_node_set.update(in_degree_cache[to_node])
                node_ans.update(t_node_set)
                node_list=t_node_set
            ans.append(sorted(node_ans))
        return ans 

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 从入度的角度去做，首先找到那些入度为0的元素，他的所有祖先都已经计算完毕了
        in_degree_count=defaultdict(lambda: 0)
        ans_path=defaultdict(set) # 记录child 的所有父亲节点
        graph_adj=defaultdict(set) # 记录parent 包含的儿子
        for parent,child in edges:
            in_degree_count[child]+=1
            ans_path[child].add(parent)
            graph_adj[parent].add(child)
        zero_degree_node=[node_id for node_id in range(n) if in_degree_count[node_id]==0]
        while zero_degree_node:
            z_node=zero_degree_node.pop(0)
            for child in graph_adj[z_node]:
                ans_path[child].update(ans_path[z_node])# 把父亲的所有节点。
                # 儿子节点入度减一
                in_degree_count[child]-=1
                if in_degree_count[child]==0:
                    zero_degree_node.append(child)
        return [ sorted(list(ans_path[i])) for i in range(n)]




