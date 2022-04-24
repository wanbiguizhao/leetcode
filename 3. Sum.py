from typing import List
from xmlrpc.client import TRANSPORT_ERROR
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 自己一直有，左边固定，右边固定，然后从中间开始找的想法
        if len(nums)<2:
            return []
        nums.sort()
        beg_index=0
        end_index=len(nums)-1
        ans=[]
        for index in range(len(nums)-2):
            if index>0 and nums[index-1]==nums[index]:
                continue 
            beg_index=index+1
            end_index=len(nums)-1
            
            while beg_index<end_index:
                target= 0 - nums[beg_index]-nums[end_index]
                if target==nums[index]:
                    ans.append(
                        [
                            target,
                            nums[beg_index],
                            nums[end_index]
                        ]
                    )
                    while beg_index<end_index and nums[beg_index]==nums[beg_index+1]:
                        beg_index+=1
                    while beg_index<end_index and nums[end_index]==nums[end_index-1]:
                        end_index-=1
                    beg_index+=1
                    end_index-=1
                elif target<nums[index]:
                    end_index-=1
                else:
                    beg_index+=1

        return ans 
if __name__ == "__main__":
    instance = Solution()
    # print(instance.myAtoi("---111"),-111)
    # print(instance.myAtoi("-+12"),12)
    # print(instance.myAtoi("-+12--"),12)
    # print(instance.myAtoi("-+000120--"),120)
   # print(instance.threeSum(nums = [-1,0,1,2,-1,-4]))
    print(instance.threeSum(nums = [4,-1,0,1,2,2,-1,-4]))