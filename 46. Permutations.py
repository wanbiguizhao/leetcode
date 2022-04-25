from typing import List 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
if __name__ == "__main__":
    instance=Solution()
    print(instance.permute([1,2,3]))
    print(instance.permute([1,2]))