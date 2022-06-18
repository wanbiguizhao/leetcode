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
        mid=(left+right+1)//2
        # reverse [:mid]
        i,j=0,mid-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        i,j=mid+1,right
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

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
        # 怎么做也是错的，放弃了 
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()# 只能想到一个O(1)空间存储复杂度的算法。
        mid=(len(nums)+1)//2
        left,right=nums[:mid],nums[mid:]
        nums[::2]=left[::-1]
        nums[1::2]=right[::-1]
        