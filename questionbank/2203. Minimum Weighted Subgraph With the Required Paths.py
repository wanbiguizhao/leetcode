
import functools
from numbers import Integral
from click import FloatRange
import pysnooper
from typing import List
from copy import copy
import heapq
from collections import defaultdict
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(start_node_id,adj_info_list):
            dist=[UPLIMIT]*n
            priority_queue=[]
            priority_queue.append((0,start_node_id))

            while priority_queue:
                data=heapq.heappop(priority_queue)
                distance,node_id = data
                if dist[node_id]<UPLIMIT:
                    continue 
                dist[node_id]=distance
                for  adj_info  in  adj_info_list[node_id]:
                    distance_adj ,adj_node_id= adj_info
                    if dist[adj_node_id]<UPLIMIT:
                        continue 
                    heapq.heappush(priority_queue,(distance_adj+distance,adj_node_id))
            return dist 
        
        ans=0
        next_adj_info=defaultdict(list)
        prev_adj_info=defaultdict(list)
        for edge in edges:
            start,end,weight = edge 
            next_adj_info[ start ].append((weight,end))
            prev_adj_info[ end ].append(( weight,start  ))  
            ans = ans + weight
        UPLIMIT=ans*2 
        ans=UPLIMIT
        shortest_info_src1_info=dijkstra(src1,next_adj_info)
        shortest_info_src2_info=dijkstra(src2,next_adj_info)
        shortest_info_dest_info=dijkstra(dest,prev_adj_info)


        for node_index in range(n):
            ans=min(
                
                    ans,
                    shortest_info_src1_info[node_index]+
                    shortest_info_src2_info[node_index]+
                    shortest_info_dest_info[node_index]
                
                )
        if ans ==UPLIMIT:
            return -1 
        return ans 

if __name__=="__main__":
    instance=Solution()
    ans=instance.minimumWeight(6,
        [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]],
        0,
        1,
        5)

        



