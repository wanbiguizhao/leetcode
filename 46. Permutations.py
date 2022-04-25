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
        # 层次遍历
        result=[nums]
        const_len=len(nums)
        for i in range(const_len):
            tmp=[
            ]
            for one_state in result:
                for j in range(i+1,const_len):
                    copy_state=one_state.copy()
                    copy_state[i],copy_state[j]=copy_state[j],copy_state[i]
                    tmp.append(
                        copy_state
                    )
            result+=tmp

        return result 
if __name__ == "__main__":
    instance=Solution()
    print(instance.permute([1,2,3]))
    print(instance.permute([1,2]))