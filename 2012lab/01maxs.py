
from typing import List
from collections import Counter,defaultdict
class Solution:
    def run(self, task_list: List[List[int]]) -> int:
        assert len(task_list)>0
        sorted_task_list=sorted(task_list)# shengxu
        time_point_set=set()
        for task in task_list: 
            # 记录任务列表的边界值
            time_point_set.add(task[0])#[task[0]]=0
            time_point_set.add(task[1])# 记录一个时间节点
            # 记录时间点
        time_point_list=sorted(list(time_point_set))
        time_point_max_count=defaultdict(int)
        for inex,task in enumerate(sorted_task_list):
                for time_point in time_point_list:
                    if task[0]<=time_point and task[1]>=time_point:
                        # 如果这个任务开始和结束时间跨越了某个点，那么就可以
                        time_point_max_count[time_point]+=task[2]
                    # 剪枝处理
                    elif time_point>task[1]:
                        break
        return max(time_point_max_count.values())
s=Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
    ]
print(s.run(matrix))
matrix = [
   [ 1,  14,  9],
   [10, 11, 13],
   [12, 13, 15]
    ]
print(s.run(matrix))
matrix = [
   [ 1,  14,  9],
    ]
print(9,s.run(matrix))
matrix = [
   [ 1,  14,  9],
   [ 3, 5 ,  10],
    ]
print(19,s.run(matrix))
matrix = [
   [ 1,  14,  9],
   [ 3, 5 ,  10],
    [ 4,  24,  9],
    [ 39,  100,  100],
    ]
print(100,s.run(matrix))