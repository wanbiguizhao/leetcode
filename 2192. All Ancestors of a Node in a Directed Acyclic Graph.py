from collections import defaultdict
from typing import List 
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
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