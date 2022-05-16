from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i], dp[j]+1)
        return max(dp)
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binselect_left(x):
            low=0
            high=len(dp)
            pos=high
            # 搜索到，满足 x<dp[i]的最小min[i]
            while low < high:
                mid=(low+high)//2 
                mid_value=dp[mid]
                if  x<mid_value:
                    high=mid
                    pos=high
                else:
                    low=mid+1
            
            return pos 
        if not nums:
            return 0
        dp=[nums[0]]
        for num in nums:



        return len(dp)