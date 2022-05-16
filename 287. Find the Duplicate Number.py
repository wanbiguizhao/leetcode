from typing import List

from sklearn import multiclass
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 原来的想法， 通过 sum(nums) 和 n(n+1)/2 之差的想法是错误的，因为可能重复不止两次
        ans=0
        for num in nums:
            x_num=abs(num)
            if nums[x_num]<0:
                ans=x_num
                break 
            nums[x_num]=nums[x_num]*-1
        # 恢复到原来的情况。
        for index in range(len(nums)):
            nums[index]=abs(nums[index])
        return ans 
        
            

                