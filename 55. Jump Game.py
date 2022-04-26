from typing import List 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        const_len=len(nums)
        nums[-1]=True
        index=const_len-2 
        while index>=0:
            max_jump=nums[index]+index
            nums[index]=False
            if max_jump>= const_len :
                nums[index]=True
                index-=1
                continue  
            #reached_flag=False
            while max_jump>index:
                if nums[max_jump]:
                    nums[index]=True
                    #reached_flag=True
                    break  
                max_jump-=1
            index-=1
        return nums[0]
if __name__ == "__main__":
    instance=Solution()
    print(instance.canJump([0]))
    print(instance.canJump([1]))
    print(instance.canJump([1,2,0]))
    print(instance.canJump([0,2,0]))
    print(instance.canJump([1,2,0,1,2,0]))
                