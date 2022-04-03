from filecmp import cmp
import imp
from typing import List 
from functools import reduce
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        
        def filter(data,filter_index):
            data=sorted(data,key=lambda x : x[filter_index:]+x[0:filter_index])
            new_data=[]
            new_data.append(data[0])
            for d in data:
                if new_data[-1][filter_index]!=d[filter_index]  :
                    new_data.append(d)
            return new_data
        # 优化，过滤那些用不上的轮子。
        tires=reduce(filter,[tires,0,1])
        cost_lap_th_cache=[0]
        for lap_th in range(1,min(16,numLaps)+1):
            cost_lap_th_cache.append(
                min([ fi*(ri**(lap_th)-1)/(ri-1) for fi,ri in tires ])
            )
        dp=[0]*(numLaps+2)
        for lap_th in range(1,numLaps+1):
            dp[lap_th]=dp[lap_th-1]+cost_lap_th_cache[1]+ (changeTime if lap_th>1  else 0)
            for j in range(1, min(lap_th,16)+1):
                dp[lap_th]=min( 
                    dp[lap_th], 
                    dp[lap_th-j]+ (0 if j==lap_th else changeTime) + cost_lap_th_cache[j] 
                    )
        return int(dp[numLaps])
if __name__=="__main__":
    solution=Solution()
    ans=solution.minimumFinishTime([[2,3],[5,4],[3,4],[2,2]],5,4)
    print(ans)