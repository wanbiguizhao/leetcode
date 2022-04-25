from turtle import right
from typing import List
class Solution:
    def searchRange_2(self, nums: List[int], target: int) -> List[int]:
        # 二分搜索
        if not nums:
            return [-1,-1]
        left_index=0
        right_index=len(nums)-1
        while left_index<=right_index:
            mid_index= (left_index+right_index)//2
            if nums[mid_index]==target:
                left=mid_index
                while left>=0 and nums[left]==target:
                    left-=1
                right=mid_index
                while right<len(nums) and nums[right]==target:
                    right+=1
                return [left+1,right-1]
            elif nums[mid_index]>target:
                right_index=mid_index-1
            else:
                left_index=mid_index+1
        return [-1,-1]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLowBound(nums,target):
            left=0
            right=len(nums)
            while left<right:
                mid=(right-left)//2+left 
                if nums[mid]==target:
                    right=mid
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid

            return left 
        def findUpBound(nums,target):
            left=0
            right=len(nums)
            while left<right:
                mid=(right-left)//2+left 
                if nums[mid]==target:
                    left=mid+1
                elif nums[mid]>target:
                    right=mid
                else:
                    left=mid+1 
            return left
        low_index=findLowBound(nums,target)
        if not nums or low_index==len(nums) or nums[low_index]!=target: # 检查边界情况
            return [-1,-1]
        up_index=findUpBound(nums,target)
        return [low_index,up_index-1]

if __name__ == "__main__":
    instance=Solution()
    #instance.search([4,5,6,7,8,1,2,3],8)
    print(instance.searchRange([6,6,6,6],6))
    print(instance.searchRange([6],6))
    print(instance.searchRange([6],5))