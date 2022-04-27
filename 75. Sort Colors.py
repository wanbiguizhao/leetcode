from turtle import left
from typing import List 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        之前做过，使用双指针,left_index 表示当前0对应的元素的最右索引，red [0,left_index] blue[right_index,n-1]
        剩下的就是中间的颜色.
        教训：不要修改没有探索到的变量。
        例如：
        """
        const_len=len(nums)
        left_index=-1
        right_index=const_len
        for index in range(const_len):
            if nums[index]==0:
                left_index+=1
            elif nums[index]==2:
                right_index-=1
                # nums[right_index]=2  教训：不要修改没有探索到的变量。试试才是案例[2,1]
        for index in range(const_len):
            if index<=left_index:
                nums[index]=0
            elif index<right_index:
                nums[index]=1
            else:
                nums[index]=2
       # print(nums)
        return 

if __name__ == "__main__":
    instance=Solution()
    # instance.sortColors([0,1,2,0],[3,4,5,2],[1,3,1,5])
    # instance.sortColors([0,1,2,0],[3,4,5,2],[1,3,1,5])
    instance.sortColors([1,0,2])
    instance.sortColors([1])
    instance.sortColors([2])
    instance.sortColors([0])
    instance.sortColors([1,0])
    instance.sortColors([0,1])
    instance.sortColors([1,2])
    instance.sortColors([2,1])
        