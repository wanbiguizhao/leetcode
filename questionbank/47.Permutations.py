from typing import List 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(res)==len(nums):
                ans.append(res[::])
                #print(ans)
            for i in range(len(nums)):
                if vis[i] or (i>0 and nums[i]==nums[i-1] and not vis[i-1]):
                    continue
                vis[i]=True 
                res.append(nums[i])
                backtrack()
                res.pop(-1)
                vis[i]=False
        res=[]
        ans=[]
        vis=[False]*len(nums)
        nums.sort()
        backtrack()
        return ans 
# instance=Solution()
# instance.permuteUnique([1,1,2])