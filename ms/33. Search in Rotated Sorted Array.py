from typing import List 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg,end=0,len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            if nums[mid]==target:
                return mid 
            elif nums[mid]<nums[end]:
                # 右侧的位置是连续的上升的
                if  target>nums[mid] and target<=nums[end]:
                    beg=mid+1
                else:
                    end=mid-1 
            else:
                if target>=nums[beg] and target<nums[mid]:
                    end=mid-1
                else :
                    beg=mid+1
        return -1

def wrongCase0(instance:Solution=Solution()):
    res=instance.search([3,5,1],3)
    print(res)


if __name__ =="__main__":
    
    wrongCase0()