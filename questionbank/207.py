class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges=collections.defaultdict(list)
        visited=[0]*numCourses
        result=list()
        self.valid=True 
        for info in prerequisites:
            edges[info[1]].append(info[0])
        def dfs(u:int):
            visited[u]=1
            for v in edges[u]:
                if visited[v]==0:
                    dfs(v)
                    if not self.valid:
                        return
                elif visited[v]==1:
                    self.valid=False
                    return
            visited[u]=2
            result.append(u)
        for i in range(numCourses):
            if self.valid and not visited[i]:
                dfs(i)
        return self.valid


        