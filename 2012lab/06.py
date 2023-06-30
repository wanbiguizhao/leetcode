
from typing import List
from collections import Counter,defaultdict
import functools
class Solution:
    # tag: 链表
    def run(self,head,node_num,node_list ) -> int:
        node_info=dict()
        head_node_key=head
        for node in node_list:
            node_key,value,next_key=node[0],node[1],node[2]
            node_info[node_key]=[value,next_key]
        next_node=0
        size=0
        current_node=head_node_key
        while current_node!=-1:# 找到实际的size。
            current_node=node_info[current_node][-1]
            size+=1
        mid_size=size//2
        target_node=node_info[head_node_key]
        cur=0
        while cur<mid_size:
            target_node=node_info[target_node[-1]]
            cur+=1
        return target_node[0]

s=Solution()
print(
    s.run(4,4,[
        [4,101,5],
        [5,105,7],
        [7,107,6],
        [6,106,-1]
    ])
)
print(
    s.run(4,5,[
        [4,101,5],
        [5,105,7],
        [7,107,6],
        [6,106,8],
        [8,108,-1]
    ])
)
print(
    s.run(4,6,[
        [4,101,5],
        [5,105,7],
        [7,107,6],
        [6,106,8],
        [8,108,10],
        [10,110,-1]
    ])
)