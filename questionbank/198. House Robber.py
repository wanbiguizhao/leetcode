from typing import List 
class Solution:
    def rob(self, nums: List[int]) -> int:
        const_len=len(nums)
        if const_len<=2:
            return max(nums)
        dp=[0]*const_len
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        index=2
        while index<const_len:
            dp[index]=max(dp[index-1],dp[index-2]+nums[index] )
            index+=1
        return dp[const_len-1]