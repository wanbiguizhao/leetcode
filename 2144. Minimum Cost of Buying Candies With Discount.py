from cmath import cos
from typing import List 
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # 贪心算法
        cost.sort(reverse=True)#排序降序
        i=0
        ans=0 
        while i+2<len(cost):
            ans+=cost[i]
            ans+=cost[i+1]
            i+=3
        if i<len(cost):
            ans+=cost[i]
            i+=1
        if i<len(cost):
            ans+=cost[i]
        return ans 

if __name__=="__main__":
    instance=Solution()
    print( instance.minimumCost([1]) ==1)
    print(instance.minimumCost([2,1])==3)
    print(instance.minimumCost([1,2,3])==5)

