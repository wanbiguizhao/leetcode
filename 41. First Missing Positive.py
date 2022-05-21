from typing import List 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 自己的思路： 对数据把大于零的放到前半段
        # 小于等于零的放到后半段
        # 然后前端段 根据数值，设置-值，
        # 然后依次遍历找到第一个大于零的值，就是结果
        # 不好处理0的问题。
        left_index,right_index=0,len(nums)-1 
        while left_index<right_index:
            while left_index<right_index and nums[left_index]>0:
                left_index+=1
            while right_index>left_index and nums[right_index]<=0:
                right_index-=1
            if left_index<right_index:
                nums[left_index],nums[right_index]=nums[right_index],nums[left_index]
                left_index+=1
                #right_index-=1
        # 确保nums[:left_index)都是大于0的正数。
        if nums[left_index]>0:
            left_index+=1
        for index in range(left_index):
            x_index_num=abs(nums[index])-1
            if x_index_num>=0 and x_index_num<left_index and nums[x_index_num]>0:
                nums[x_index_num]=-nums[x_index_num]
        for index in range(left_index):
            if nums[index]>0:
                return index+1
        return left_index+1 
    def firstMissingPositive_2(self, nums: List[int]) -> int:
        # 核心问题是减少非正数的干扰。
        for i,num in enumerate(nums):
            if num <= 0:
                nums[i] = 0
        for i,num in enumerate(nums):
            index = abs(num) - 1
        if index >=0 and index<len(nums):
            if nums[index] == 0:
                num[index] = "-inf"
            elif nums[index] >0:
                nums[index]=-nums[index]
        for index,num in enumerate(num):
            if num>=0:
                return index + 1
        return len(nums)+1 

if __name__ == "__main__":
    instance=Solution()
    instance.firstMissingPositive([1,2,0])
    instance.firstMissingPositive([-1,2,0,-1])