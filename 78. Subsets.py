from typing import List 
from copy import copy
class Solution:
    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        #  方法1 DFS
        def _subsets(i_th:int,pre_ans:List[int]):
            if i_th==len(nums):
                ans.append(pre_ans)# 这里可以不复制
                return 
            _subsets(i_th+1,pre_ans)
            _subsets(i_th+1,pre_ans+[nums[i_th]])
        ans=[]
        _subsets(0+1,[])
        _subsets(0+1,[nums[0]])
        #print(ans)
        return ans 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #  方法2 状态回溯法，不使用递归

        ans=[[]]
        index=0
        while index<len(nums):
            round_ans=[]
            for one_ans in ans:
                round_ans.append(
                    one_ans+[]
                )
                round_ans.append(
                    one_ans+[ nums[index] ]
                )
            ans=round_ans
            index+=1
        print(ans)
        return ans 

        
if __name__ == "__main__":
    instance=Solution()
    instance.subsets([0])
    instance.subsets([0,1,3])