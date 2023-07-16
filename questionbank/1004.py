
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros=0
        left,right=0,0
        ans=0
        while right<len(nums):
            if nums[right]==0:
                zeros+=1
            while k<zeros:
                if nums[left]==0:
                    zeros-=1
                left+=1
            ans=max(ans,right-left+1)
            right+=1
        return ans 

