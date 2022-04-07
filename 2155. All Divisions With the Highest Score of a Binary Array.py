from typing import List
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero_ans=[0]*(len(nums)+1)
        for index in range(1,len(nums)+1):
            num=nums[index-1]
            zero_ans[index]=zero_ans[index-1]
            if num==0:
                zero_ans[index]=zero_ans[index-1]+1
                #
        one_ans=[0]*(len(nums)+1)
        for index in reversed(range(0,len(nums))):
            num=nums[index]
            one_ans[index]=one_ans[index+1]
            if num==1:
                one_ans[index]=one_ans[index+1]+1
        for index in range(len(nums)+1):
            zero_ans[index]+=one_ans[index]
        max_score=max(zero_ans)
        ans=[ index for index, score in enumerate(zero_ans) if score ==max_score  ] 
        return ans 
        
if __name__=="__main__":
    solution=Solution()
    ans=solution.maxScoreIndices([0,0,1,0])
    print(ans,ans==[2,4])
        
