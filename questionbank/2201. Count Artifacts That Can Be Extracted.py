from unittest import installHandler
import pysnooper
from typing import List 

class Solution:
    # user cache 
    # 以后要总结自己的代码和高质量代码的区别。
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        def convert(arear:List)->List[int]:
            r1 , c1 , r2 , c2 = arear
            for r_coord in range(r1,r2+1):
                for c_coord in range(c1,c2+1):
                    yield "{}-{}".format(r_coord,c_coord)

        ans = 0 
        cache_dig = set()
        for dig_arear in dig :
            cache_dig.add("{}-{}".format(dig_arear[0],dig_arear[1]))
        for arear in artifacts:
            hit_flag=all([ x in cache_dig for x in convert(arear)])
            if hit_flag:
                ans+=1
        return ans

if __name__ == "__main__":
    instance=Solution()
    # instance.digArtifacts(2,artifacts=[[0,0,0,0],[0,1,1,1]],dig=[[0,0],[0,1]] )
    # instance.digArtifacts(2,artifacts=[[0,0,0,0],[0,1,1,1]],dig=[[0,0],[0,1],[1,0]] )
    # instance.digArtifacts(2,artifacts=[[0,0,0,0],[0,1,1,1]],dig=[[0,0],[0,1],[1,1]] )
#     instance.digArtifacts(5,
# [[3,1,4,1],[1,1,2,2],[1,0,2,0],[4,3,4,4],[0,3,1,4],[2,3,3,4]],
# [[0,0],[2,1],[2,0],[2,3],[4,3],[2,4],[4,1],[0,2],[4,0],[3,1],[1,2],[1,3],[3,2]] )
    instance.digArtifacts(6, 
   [[0,2,0,5],[0,1,1,1],[3,0,3,3],[4,4,4,4],[2,1,2,4]],
[[0,2],[0,3],[0,4],[2,0],[2,1],[2,2],[2,5],[3,0],[3,1],[3,3],[3,4],[4,0],[4,3],[4,5],[5,0],[5,1],[5,2],[5,4],[5,5]])