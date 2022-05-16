from typing import List 
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
        while x<=amount:
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
                                cache[x]=cache[x-coin]
                    else:
                        break 
            
        if amount in cache:
            return cache[amount]
        return -1

