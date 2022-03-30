import re
import pysnooper
from typing import List
from copy import copy
# 贪心算法
# k is kth nus from 1 
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        ans = -1 
        if len(nums)==1:
            if k%2 ==1 :
                return ans
            else:
                return nums[0]
        

        if k>len(nums):
            ans = max(nums)
        elif k==len(nums):
            ans = max(nums[:k-1])
        else: 
            if k-1>0:
                ans=max(nums[:k-1])
            ans=max(ans,nums[k])         
        return ans 
if __name__=="__main__":
    instance=Solution()
    ans=instance.maximumTop([1,2],3)
    ans=instance.maximumTop([1,2],2)
    ans=instance.maximumTop([1,2],1)
    ans=instance.maximumTop([1,2,3],2)
    ans=instance.maximumTop([1],3)