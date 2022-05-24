# 感觉又是一个滑动窗口
from typing import List
class Solution:
    # https://www.youtube.com/watch?v=XwUb7x6YDeA 官方讲解
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 暴力解法

        ans=0
        for index in range(len(heights)):
            i=j=index 
            while i>=0 and heights[i]>=heights[index]:
                i-=1
            while j<len(heights) and  heights[j]>=heights[index]:
                j+=1 
            ans=max(ans,heights[index]*(j-i-1))
        return ans 
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈方法

        heights.append(0)
        heights.insert(0,0)
        ans=0
        stack=[0]
        for index in range(1,len(heights)):
            while stack and heights[ stack[-1] ]>heights[index]:
                height_index=stack.pop()
                height=heights[height_index]
                ans=max(ans,height*(index-stack[-1]-1))
            stack.append(index)
        return ans 
if __name__ == "__main__":
    instance=Solution()
    # instance.largestRectangleArea([1,2,3])
    # instance.largestRectangleArea([1,2,3,3,2,1,1,1,1,1,1,1])
    instance.largestRectangleArea([2,1,2])
    instance.largestRectangleArea([0])