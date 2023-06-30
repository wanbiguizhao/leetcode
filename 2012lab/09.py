
from typing import List
from collections import Counter,defaultdict
import functools
class Solution:
    # tag: 链表
    def run(self,num_str,block_str ) -> int:
        def dfs(index,mid_result):
            # 深度优先遍历
            if index==len(num_str):
                # 达到条件返回结果
                ans.append("".join(mid_result))
                return
            num_char_list=num_char_map[num_str[index]]
            for ch in num_char_list:
                dfs(index+1,block_str+[ch])
        ans=[]
        num_char_map={
            "0":"abc",
            "1":"def",
            "2":"ghi"
        }
        dfs(0,ans)
        return [ one for one in ans if one not in block_str]
