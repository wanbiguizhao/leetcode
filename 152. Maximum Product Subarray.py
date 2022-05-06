from mimetypes import suffix_map
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    # 没有零的情况
    # 假如有偶数个负数，那么结果为所用的元素之和。
    # 假如有奇数个负数，看负数的左边连乘，看负数的右边连乘都是正数
    # 假如有零的情况
    # 有零的元素的连乘归于0，变成了子问题（不包含零的nums）进行计算。  
        if len(nums)==1:
            return nums[0]
        prefix_product=1
        ans=nums[0]
        for num in nums:
            prefix_product=prefix_product*num
            ans=max(ans,prefix_product)
            if prefix_product==0:
                prefix_product=1
        suffix_product=1
        for num in nums[::-1]:
            suffix_product=suffix_product*num 
            ans=max(ans,suffix_product)
            if suffix_product==0:
                suffix_product=1
        return ans 

