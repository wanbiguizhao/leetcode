from typing import List

from cv2 import rotate
from sklearn.svm import NuSVC
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        翻转方法
        """
        def _rotate(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
            return
        k=k%len(nums) 
        if k==0:
            return 
        _rotate(0,len(nums)-k-1)
        _rotate(len(nums)-k,len(nums)-1)
        _rotate(0,len(nums)-1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        单独循环移动移动法
        每次移动，看成有若干个圈，
        https://zhuanlan.zhihu.com/p/143521482
        """
        k=k%len(nums) 
        if k==0:
            return 
        move_step=0
        beg_index=0
        while move_step<len(nums):
            
            current_index=beg_index
            tmp_val=nums[current_index]
            while True:
                next_index=(current_index+k)%len(nums)
                tmp_val,nums[next_index]=nums[next_index],tmp_val
                move_step+=1
                current_index=next_index
                if current_index==beg_index:
                    beg_index+=1
                    break



        