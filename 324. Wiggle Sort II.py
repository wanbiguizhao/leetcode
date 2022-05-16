from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()# 只能想到一个O(1)空间存储复杂度的算法。
        # 排序，
        # 后半截的数字依次插入前半截
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        big_index=mid+1
        small_index=1
        while big_index<=right:
            tmp=nums[big_index]
            index=big_index-1
            while index>=small_index:
                nums[index+1]=nums[index]
                index-=1
            nums[small_index]=tmp
            small_index+=2
            big_index+=1

        