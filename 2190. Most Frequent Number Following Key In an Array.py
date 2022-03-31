import math
from socket import errorTab 
import pysnooper
from collections import defaultdict
from typing import List 
import math 
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        key_bulket=[0]*1001
        ans=ans_count=0
        for index,num in enumerate(nums[:-1]):
            if key==num:
                
                target=nums[index+1]
                key_bulket[target]+=1
                if key_bulket[target]>ans_count:
                    ans=target
                    ans_count=key_bulket[target]
        return ans 

if __name__=="__main__":
    solution=Solution()
    solution.mostFrequent([1,1000,2],1000)