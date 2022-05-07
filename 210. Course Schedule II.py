from typing import List 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs，首先遍历入度为零的节点，处理找到新的入度为零的节点，然后知道结束。
        indegree_dict={courses_id:0 for courses_id in range(numCourses) }
        outdegree_list_dict={courses_id:[] for courses_id in range(numCourses)}
        # init data 
        ans=[]
        for req in prerequisites:
            # req[1] 完成后才能学req[0]
            indegree_dict[req[0]]+=1 # req[0] 依赖的课程数
            outdegree_list_dict[req[1]].append(req[0]) # 学完req[1] 之后可以学的课程
        zero_list=[couserid for couserid, indegree in  indegree_dict.items() if indegree==0 ]
        while zero_list:
            couserid=zero_list.pop(0)
            ans.append(couserid)
            for nextid in outdegree_list_dict[couserid]:
                indegree_dict[nextid]-=1
                if indegree_dict[nextid]==0:
                    zero_list.append(nextid)
        if len(ans)!=numCourses:
            return []
        return ans 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs，首先遍历入度为零的节点，处理找到新的入度为零的节点，然后知道结束。
        indegree_dict={courses_id:0 for courses_id in range(numCourses) }
        outdegree_list_dict={courses_id:[] for courses_id in range(numCourses)}
        # init data 
        ans=[]
        for req in prerequisites:
            # req[1] 完成后才能学req[0]
            indegree_dict[req[0]]+=1 # req[0] 依赖的课程数
            outdegree_list_dict[req[1]].append(req[0]) # 学完req[1] 之后可以学的课程
        zero_list=[couserid for couserid, indegree in  indegree_dict.items() if indegree==0 ]
        left_index=0
        right_index=len(zero_list)-1
        while left_index<=right_index:
            couserid=zero_list[left_index]
            left_index+=1
            #ans.append(couserid)
            for nextid in outdegree_list_dict[couserid]:
                indegree_dict[nextid]-=1
                if indegree_dict[nextid]==0:
                    zero_list.append(nextid)
                    right_index+=1
        if len(zero_list)!=numCourses:
            return []
        return zero_list 

if __name__ == "__main__":
    instance=Solution()
    instance.findOrder(numCourses = 2, prerequisites = [[1,0]])
    instance.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
    instance.findOrder(numCourses = 1, prerequisites = [])
    instance.findOrder(numCourses = 5, prerequisites = [[0,1],[1,0]])