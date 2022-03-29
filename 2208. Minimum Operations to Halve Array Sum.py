from heapq import *
from typing import List
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sum_nums=sum(nums)
        half_sum_nums=sum_nums/2.0
        convert_nums=list(map(lambda x:-1*x,nums))
        heapify(convert_nums)
        
        ans=0
        while half_sum_nums>0:
            max_value=convert_nums[0]
            half_sum_nums+=max_value/2.0
            heappushpop(convert_nums,max_value/2)
            ans+=1
        return ans 
if __name__ == "__main__":
    instance = Solution()
    # instance.longestRepeating("babaccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"*200,"bcb",[1,3,3])
    ans=instance.halveArray([10,2,3,8])   
    print(ans)
