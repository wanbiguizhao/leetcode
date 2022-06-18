from typing import List 
class Solution:
    def trap(self, height: List[int]) -> int:
        # 1.  对于元素i，高度为height[i]
        # 2. 左边的情况找到最高的元素left_max_height
        # 3. 右边可以找到最高的边right_max_height
        # 4. 元素i可以保留的水是:max(0,min(left_max_height,right_max_height)-height[i])
        const_height_len=len(height)
        left_max_list=[0]*const_height_len
        left_max_list[0]=height[0]
        right_max_list=[0]*const_height_len
        right_max_list[const_height_len-1]=height[const_height_len-1]
        for index in range(1,const_height_len-1):
            left_max_list[index]=max(height[index-1],left_max_list[index-1])
        for index in range(const_height_len-2,0,-1):
            right_max_list[index]=max(height[index+1],right_max_list[index+1])
        ans=0
        for index in range(1,const_height_len-1):
            ans+=max( min(left_max_list[index],right_max_list[index]) -height[index] ,0)
        return ans 
if __name__ == "__main__":
    instance=Solution()
    instance.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
    instance.trap(height =[4,2,0,3,2,5])