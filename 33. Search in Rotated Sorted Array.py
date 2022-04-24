from turtle import left
from typing import List 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index=0
        right_index=len(nums)-1
        while left_index<=right_index:
            # 搜索右侧
            mid_index=(left_index+right_index)//2
            if nums[mid_index]==target:
                return mid_index
            # 判断某个区间是有序的
            if nums[mid_index]<nums[right_index]:
                if target> nums[mid_index] and target<=nums[right_index] :
                    left_index=mid_index+1
                else:
                    right_index=mid_index-1
            else:
                if target>=nums[left_index] and target<nums[mid_index]:
                    right_index=mid_index-1
                else:
                    left_index=mid_index+1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        left_index=0
        right_index=len(nums)-1
        while left_index<=right_index:
            mid_index=(left_index+right_index)//2
            if nums[mid_index]==target:
                return mid_index
            # 判断某个区间是有序的
            if nums[left_index]<=nums[mid_index]:# 是不是要等于? 要因为下取整，存在left_index==mid_index的可能性
                if target> nums[mid_index] and target<=nums[right_index] :
                    left_index=mid_index+1
                else:
                    right_index=mid_index-1
            else:
                if target>=nums[left_index] and target<nums[mid_index]:
                    right_index=mid_index-1
                else:
                    left_index=mid_index+1
        return -1


if __name__ == "__main__":
    instance=Solution()
    #instance.search([4,5,6,7,8,1,2,3],8)
    instance.search([4,5,6,7,0,1,2],0)
    # print(instance.search([5,6,7,0,1,2],0))
    # print(instance.search([5,6,7,0,1,2],1))
    # print(instance.search([5,6,7,0,1,2],2))
    # print(instance.search([5,6,7,0,1,2],3))
    # print(instance.search([5,6,7,0,1,2],4))
    # print(instance.search([5,6,7,0,1,2],5))
    # print(instance.search([5,6,7,0,1,2],7))
    # print(instance.search([0],0))
    # print(instance.search([1],0))
