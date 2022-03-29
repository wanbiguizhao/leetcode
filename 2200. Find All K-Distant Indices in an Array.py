import pysnooper
from typing import List 
class Solution:
    @pysnooper.snoop()
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans=[]
        k_boundary_index=0
        for index,num in enumerate(nums):
            if num!=key:
                continue 
            ans_index=  max(k_boundary_index,index - k)# k_boundary_index is [0,k_boundary_index) already userless 
            while ans_index <= index + k and ans_index < len(nums):
                if ans_index>= k_boundary_index:
                    # already push to ans 
                    ans.append(ans_index)
                
                ans_index+=1
            
            k_boundary_index= ans_index
        return ans 
#  k_boundary_index 代表的就是是开区间还是闭区间，要想清楚，以后这个是非常重要的一个注意点。




if __name__=="__main__":
    solution=Solution()
    solution.findKDistantIndices([1,1,1,1,1],1,3)
    solution.findKDistantIndices([1,1,1,2,2,2,2,2,2,1,1],1,2)

    # 两个key之间覆盖的区域有交叉
    # 所有的值都一样