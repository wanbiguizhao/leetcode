from collections import Counter
from typing import List 
class Solution:
    def countElements(self, nums: List[int]) -> int:
        # 这个算法使用的单独的存储空间。
        nums_counter=Counter(nums)
        max_num=-10**5+1
        min_num=10**5-1
        for num,cnt in nums_counter.items():
            max_num=max(max_num,num)
            min_num=min(min_num,num)
        if max_num==min_num:
            return 0
        return len(nums)-nums_counter[max_num]-nums_counter[min_num]
    def countElements(self, nums: List[int]) -> int:
        # O（1） 时间复杂度 O（1） 空间复杂度
        max_num=-10**5+1
        min_num=10**5-1
        for num in nums:
            max_num=max(max_num,num)
            min_num=min(min_num,num)
        if max_num==min_num:
            return 0
        return len( [num for num in nums if num !=max_num and num !=max_num ] )