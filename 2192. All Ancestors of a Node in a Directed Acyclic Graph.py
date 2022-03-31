from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        out_degress_cache=defaultdict(list)
        in_degree_cache=defaultdict(list)
        for edge in edges:
            from_node,to_node=edge
            in_degree_cache[to_node].append(from_node)
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
        