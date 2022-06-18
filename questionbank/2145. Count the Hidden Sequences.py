
from typing import List 
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # 使用数学公式进行计算推算出 a< x<b 
        # 计算前缀和
        pre_sum=0
        for index,num in enumerate(differences):
            differences[index]=num+pre_sum
            pre_sum=differences[index]
        min_var=min(differences)
        max_var=max(differences)
        x_lower=max(lower-min_var,lower)
        x_upper=min(upper-max_var,upper)
        if x_upper<x_lower:
            return 0 
        return x_upper-x_lower+1
if __name__=="__main__":
    instance=Solution()
    ans=instance.numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper = 5)
    print(ans==4)
    ans=ans=instance.numberOfArrays(differences = [4,-7,2], lower = 3, upper = 6)
    print(ans==0)
    ans=ans=instance.numberOfArrays(differences = [-40], lower = -46, upper = 53)
    print(ans==60)