from filecmp import cmp
from typing import List 
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        new_tires=[]
        for t in sorted(tires):
            if not new_tires:
                new_tires.append(t)
                continue
            if new_tires[-1][0]!=t[0]:
                new_tires.append(t)
        tires=new_tires
        new_tires=[]
        for t in sorted(tires,key=lambda x:x[1]):
            if not new_tires:
                new_tires.append(t)
                continue
            if new_tires[-1][1]!=t[1]:
                new_tires.append(t)
        tires=new_tires
        ans=0
        cost_lap_th_cache=[0]# 
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
    ans=solution.minimumFinishTime([[2,3],[3,4]],5,4)
    print(ans)