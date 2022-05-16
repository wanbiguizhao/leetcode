from typing import Optional,List 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_fix=1
        right_fix=1
        ans=[1]*len(nums)
        for index in range(1,len(nums)):
            left_fix=left_fix*nums[index-1]
            ans[index]=left_fix
        for index in range(len(nums)-2,-1,-1):
            right_fix=right_fix*nums[index+1]
            ans[index]=ans[index]*right_fix
        #print(ans)
        return ans 
if __name__ == "__main__":
    instance=Solution()
    #instance.evalRPN(tokens = ["2","1","+","3","*"])
    instance.productExceptSelf([1,2,3,4,5,6])
    instance.productExceptSelf([4,6])
    instance.productExceptSelf([4,6,0])
    instance.productExceptSelf([4,0,6])