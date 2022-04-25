from typing import List 
class Solution:
    def permute_1(self, nums: List[int]) -> List[List[int]]:
        def _permute(x_nums,pre_ans):
            if not x_nums:
                ans.append(pre_ans)
                return 
            for index,x in enumerate(x_nums):
                _permute(x_nums[:index]+x_nums[index+1:],pre_ans+[x])

        ans=[]
        if not nums:
            return ans 
        _permute(nums,[])
        return ans 
    def permute(self, nums: List[int]) -> List[List[int]]:
        # https://www.youtube.com/watch?v=w4SjNXKLsv4
        def _permute(pre_ans:list):
            if len(pre_ans)==len(nums):
                ans.append([val for val in pre_ans] )
                return 
            for index,x in enumerate(nums):
                if state_cache[x]==1:
                    continue
                state_cache[x]=1 
                _permute(pre_ans+[x])
                state_cache[x]=0
        
        ans=[]
        if not nums:
            return ans 
        state_cache={}
        for i in range(-10,11):
            state_cache[i]=0
        _permute([])
        return ans 
if __name__ == "__main__":
    instance=Solution()
    print(instance.permute([1,2,3]))
    print(instance.permute([1,2]))