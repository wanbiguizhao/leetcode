from typing import List
from operator import lt
class Solution:
    def largestNumber_wrong(self, nums: List[int]) -> str:
        # 排序规则，首位的大小，越大越靠前
        # 长度，越小越靠前
        # 都一样的话，比大小，越大越靠前
        # 
        def split_helper(num):
            if num ==0:
                return num 
            last_num=num%10
            while num<10**9:
                num=num*10+last_num
            return num
        nums.sort(key= split_helper,reverse=True) 
        print("".join(map(str,nums)))
        return "".join(map(str,nums))
    
    def largestNumber(self,nums:List[int])-> str:
        class CMPNumber(str):
            def __init__(self,num) -> None:
                self.num=num 
            def __lt__(self,x):
                return self.num+x>x+self.num
        if not any(nums):# 全零
            return "0" 
        return "".join(
           sorted( map(str,nums),key=CMPNumber)
            )


if __name__ == "__main__":
    instance=Solution()
    instance.largestNumber([3,30,34,5,9])
    instance.largestNumber([0])
    instance.largestNumber([0,30])