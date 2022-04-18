from typing import List 
from collections import Counter
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums_counter=Counter(nums)
        ans=[]
        for num,count in nums_counter.items():
            if count==1 and nums_counter[num+1]==0 and nums_counter[num-1]==0:
                ans.append(num)
        return ans 
            