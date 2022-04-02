from typing import List 
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_time_cost_down=0
        min_time_cost_up=time[0]*totalTrips+1 # 先找到一个答案然后再进行优化
        ans=min_time_cost_up
        #min_time_cost->[] 前闭后闭区间
        while min_time_cost_down<=min_time_cost_up:
            mid_cost=(min_time_cost_up+min_time_cost_down)//2
            if totalTrips> sum([ mid_cost//t for t in time]):## 返回规定时间内，能运行的trips
                min_time_cost_down=mid_cost+1
            elif totalTrips<=sum([ mid_cost//t for t in time]):
                min_time_cost_up=mid_cost-1
                ans=mid_cost
        return ans 

            


         

if __name__=="__main__":
    solution=Solution()
    ans=solution.minimumTime([1],5)
    print(ans)
    ans=solution.minimumTime([1,2],5)
    print(ans)
    ans=solution.minimumTime([1,2,3],5)
    print(ans)
    ans=solution.minimumTime([1,2,3],6)
    print(ans)
