#import pysnooper
from typing import List
from collections import defaultdict
import math 
class Solution:
    #@pysnooper.snoop()
    def countPairs(self, nums: List[int], k: int) -> int:
        division_num_set=set()
        division_num=1
        while division_num*division_num<=k:
            if k%division_num==0:
                division_num_set.add(division_num)
                division_num_set.add(k//division_num)
            division_num+=1
        # 目前是所有约数。
        num_index_cache=defaultdict(int)
        ans=0
        for num_index,num_value in enumerate(nums):
            gcd=math.gcd(k,num_value)
            target_divisor=k//gcd
            ans+=num_index_cache[target_divisor]
            # 从num_index 开始向前搜索，你不知道未知的情况，但是可以回头看  num_Index 之前的情况

            for k_divisor in division_num_set:
                if num_value%k_divisor==0:
                    num_index_cache[k_divisor]+=1
        return ans 

if __name__=="__main__":
    solution=Solution()
    ans=solution.countPairs([1,2,3,4,5],5)   
    print(ans)        
    ans=solution.countPairs([i for i in range(10000)],1)   
    print(ans)

        
        
        
        


        