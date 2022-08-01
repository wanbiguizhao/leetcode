from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans=0
        index=0 
        while index<len(nums):
            val=nums[index]
            if val<0:
                next_index=-val 
            else:
                next_index=val 
            if nums[next_index-1]<0:
                ans=next_index
                break
            else:
                nums[next_index-1]=-nums[next_index-1]
            index+=1
        index=0
        while index<len(nums):
            if nums[index]<0:
                nums[index]=-nums[index]
            index+=1
        return ans 
def testCase0(instance:Solution=Solution()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")
    res=instance.findDuplicate([1,2,4,3,4])
    print(res,res==4)
    res=instance.findDuplicate([1,2,1,3,4])
    print(res,res==1)
    res=instance.findDuplicate([1,1])
    print(res,res==1)
    res=instance.findDuplicate([2,2,2])
    print(res,res==2)
if __name__ =="__main__":
    #testCase0()
    testCase0()