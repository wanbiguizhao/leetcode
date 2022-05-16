import re
from typing import List

from urllib3 import Retry 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # pass 
        cache={0:0}
        coins.sort()# 排序，使用自底向上的方法去弄
        # 对于 [1,4,5] 8 的输入测试案例，并不能使用贪心法
        # 还是自底向上构架吧。
        for coin in coins:
            cache[coin]=1 
        ans=0
        x=coins[0]
        while x<amount:
            x+=1
            if x in cache:
                continue
            else:
                for coin in coins:
                    if x>coin:
                        if x-coin in cache:
                            if x in cache:
                                cache[x]=min(1+cache[x-coin],cache[x])
                            else:
                                cache[x]=cache[x-coin]+1
                    else:
                        break 
            
        if amount in cache:
            return cache[amount]
        return -1

def coinChange(self, coins: List[int], amount: int) -> int:
        # 尝试BFS，存在大量的重复答案。
        coins.sort()# 排序，使用自底向上的方法去弄
        # 对于 [1,4,5] 8 的输入测试案例，并不能使用贪心法
        # 还是自底向上构架吧。
        if amount==0:
            return 0
        if amount<coins[0]:
            return -1 
        ans=0 
        bfs_queue=[0]
        while bfs_queue:
            tmp_set=set()
            ans+=1
            for x in bfs_queue:
                if x>amount: # 剪枝法
                    continue
                for coin in coins:
                    if (x+coin)==amount:
                        return ans  
                    elif x+coin<amount:
                        tmp_set.add(x+coin) # 这个可能已经有过计算过的答案了
                    else:
                        break
            bfs_queue=list(tmp_set)
            bfs_queue.sort()
        return -1