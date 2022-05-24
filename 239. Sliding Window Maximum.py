from typing import List 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=[] # 存放val和index  确认一下出栈的规则 和入栈的规则 ，单调下降栈
        ans=[]
        if k==len(nums):
            return [max(nums)]
        for index in range(k):
            num=nums[index]
            while stack and stack[-1][1]<num:
                stack.pop(-1)
            stack.append([index,num])
        ans.append(stack[0][1])
        for index in range(k,len(nums)):
            num=nums[index]
            if stack and index- stack[0][0]>=k:
                stack.pop(0)
                # 出栈了
                # 会出多个元素的栈吗？
            while stack and stack[-1][1]<num:
                stack.pop(-1)
            stack.append([index,num])
            ans.append(stack[0][1])
        return ans 

if __name__ == "__main__":
    instance=Solution()
    # instance.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
    # instance.maxSlidingWindow(nums = [1], k = 1)
    # instance.maxSlidingWindow(nums = [1,2,3,3,3,3,5], k = 3)
    instance.maxSlidingWindow(nums = [7,2,4], k = 2)
