from typing import List
from collections import defaultdict 
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def product(numsA,numsB):
            ans_dict=defaultdict(0)
            for a in numsA:
                for b in numsB:
                    ans_dict[a+b]+=1
            return ans_dict 
        add_12_dict=product(nums1,nums2)
        add_34_dict=product(nums3,nums4)
        ans=0
        for val,cnt in add_12_dict.items():
            if -val in add_34_dict:
                ans+=cnt*add_34_dict[-val]
        return ans 
        