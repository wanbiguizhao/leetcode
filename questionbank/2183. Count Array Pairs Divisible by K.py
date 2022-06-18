#import pysnooper
from typing import Counter, List
from collections import defaultdict
import math 
class Solution:
    #@pysnooper.snoop()
    def countPairs_2(self, nums: List[int], k: int) -> int:
        division_num_set=set()
        division_num=1
        while division_num<=k:
            if k%division_num==0:
                division_num_set.add(division_num)
                #division_num_set.add(k//division_num)
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

    def countPairs(self, nums: List[int], k: int) -> int:
        # 排列组合的思想+gcd
        ans=0
        gcd_counter=Counter([ math.gcd(k,num) for num in nums  ])
        # 每个num都对应一个gcd 
        # 选取两个数据
        for gcd_n1 ,gcd_n1_count in gcd_counter.items():
            for gcd_n2 ,gcd_n2_count in gcd_counter.items():
                if gcd_n2>gcd_n1 and gcd_n1*gcd_n2%k==0:
                    # 确保是两个数据的情况A，B；两个集合各选择一个数据
                    ans+=gcd_n1_count*gcd_n2_count
        for gcd_n,gcd_n_count in gcd_counter.items():
            # 同一个集合里面选择两个数据,C（n,2）种排列情况
            if gcd_n*gcd_n%k==0:
                ans+=gcd_n_count*(gcd_n_count-1)//2 
        return ans 

if __name__=="__main__":
    solution=Solution()
    ans=solution.countPairs([1,2,3,4,5],5)   
    print(ans)        
    ans=solution.countPairs([i for i in range(10000)],1)   
    print(ans)

        
        
        
        


        