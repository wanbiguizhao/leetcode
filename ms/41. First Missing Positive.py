from typing import List 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numsLength=len(nums)
        for index in range(numsLength):
            if nums[index]<0:
                nums[index]=0
        for index in range(numsLength):
            x=abs(nums[index])-1

            if x>=0 and x<numsLength:
                if nums[x]==0:
                    nums[x]=-numsLength-numsLength  # 这个思路好，排除了负数
                if nums[x]>0: # 防止被负负得正。wrongCase0 [1,1]
                    nums[x]=-nums[x] # 
        for index in range(numsLength):
            if nums[index]>=0:
                return index+1 
        return numsLength+1



def testCase0(instance:Solution=Solution()):
    assert instance.firstMissingPositive([1,2,3,4])==5
    assert instance.firstMissingPositive([2,3,4])==1
    assert instance.firstMissingPositive([-1,1,3,4])==2
    
def wrongCase0(instance:Solution=Solution()):
    assert instance.firstMissingPositive([0,1,2])==3
    assert instance.firstMissingPositive([1,1])==2
if __name__ =="__main__":
    testCase0()
    wrongCase0()