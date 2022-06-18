from typing import List
class Solution:
    def maxArea_no_optional(self, height: List[int]) -> int:
        # 贪心算法
        # [i,j] 是一个潜在的区域 一定有 height[j] > height[j+1,n-1]  height[i]> height[0,i-1]
        # 当 height[i]>height[j] 时，一定有height[i] >height[j+1,n-1] 
        # 同理 ，反之 height[i]《height[j]，一定有 height[j]>height[0,i-1] 
        # 运用数学分析逻辑
        left_index=0
        right_index=len(height)-1
        ans_area=0
        while left_index<right_index:
            current_area=(right_index-left_index)*min(height[left_index],height[right_index])
            ans_area=max(current_area,ans_area)
            if height[left_index]>height[right_index]:
                right_index-=1
            else:
                left_index+=1 
        return ans_area 
    def maxArea(self, height: List[int]) -> int:
        # 优化,减少不必要的比较次数
        # 运用数学分析逻辑
        left_index=0
        right_index=len(height)-1
        ans_area=0
        while left_index<right_index:
            current_area=(right_index-left_index)*min(height[left_index],height[right_index])
            ans_area=max(current_area,ans_area)
            if height[left_index]>height[right_index]:
                value=height[right_index]
                right_index-=1
                while right_index>left_index and  value>height[right_index]:
                    right_index-=1 # 优化减少比较次数
            else:
                value=height[left_index]
                left_index+=1 
                while right_index>left_index and  height[left_index]<value:
                    left_index+=1 # 优化减少比较次数
        return ans_area 
if __name__ == "__main__":
    instance = Solution()
    print(instance.maxArea([1,2]),1)
    print(instance.maxArea([1,2,3,4,5,6,9,8,22,9]),1)


