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

