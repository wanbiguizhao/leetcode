
from typing import List
from copy import copy 
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        sorted_beans=sorted(beans,reverse=True)
        pre_beans_sum=copy(sorted_beans)
        for i in range(1,len(pre_beans_sum)):
            pre_beans_sum[i]+=pre_beans_sum[i-1]
        # 记录前n个和
        remove_bean=0
        for index,bean_sum in enumerate(pre_beans_sum[1:],1):
            remove_bean=min( remove_bean + sorted_beans[index] ,bean_sum - (index+1)*sorted_beans[index] )
        return remove_bean
if __name__=="__main__":
    solution=Solution()
    # ans= solution.minimumRemoval([10])
    # print(ans,ans==0)
    # ans = solution.minimumRemoval([5,1])
    # print(ans,ans==1)
    # ans = solution.minimumRemoval([5,2,2])
    # print(ans,ans==3)
    ans = solution.minimumRemoval([4,1,6,5])
