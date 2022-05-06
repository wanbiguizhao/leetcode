from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        const_len=len(nums)
        left_index=0
        right_index=const_len-1
        # 一旦思路错了就不行了
        # 大致思路想明白了,要比较 mid+1，mid 的关系
        # 但是划分子问题的思路不正确
        while left_index<right_index:
            mid_index=(right_index- left_index)//2 +left_index
            if nums[mid_index]>nums[mid_index+1]:
                right_index=mid_index
            else:
                left_index=mid_index+1 
        return left_index


