from tkinter import N
from typing import List 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p_num_i=0
        n_num_i=1
        ans_nums=[0]*len(nums)
        for num in nums:
            if num>0:
                ans_nums[p_num_i]=num
                p_num_i+=2
            else:
                ans_nums[n_num_i]=num 
                n_num_i+=2

        return ans_nums 
