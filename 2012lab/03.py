
from typing import List
from collections import Counter,defaultdict
import functools
class Solution:
    # tag: 贪心
    # 最重的和最轻的组成一辆
    def run(self, m:int,n:int,weight_list:List[int]) -> int:
        weight_list=sorted(weight_list)
        left=0
        right=len(weight_list)-1
        min_bike=0
        while left<right:
            current_weight=weight_list[left]+weight_list[right]
            if current_weight>m:
                right-=1# 最大体重独自一辆自行车
            else:
                right-=1
                left+=1
            min_bike+=1
        if left==right:# 还剩下一个的时候
            min_bike+=1
        return min_bike
s=Solution()
print(
    s.run(10,3,[10,9,5])
)
print(
    s.run(15,3,[10,9,5])
)
print(
    s.run(15,3,[1,8,5])
)