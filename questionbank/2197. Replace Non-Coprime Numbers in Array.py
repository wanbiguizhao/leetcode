import math 
import pysnooper
from collections import defaultdict
from typing import List 
import math 
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack_gcd=[]
        for num in nums :
            continue_flag=True
            while len(stack_gcd)>=2 and continue_flag:
                top=stack_gcd[-1]
                top2=stack_gcd[-2]
                if math.gcd(top,top2)==1:
                    continue_flag=False 
                else:
                    stack_gcd.pop(-1)
                    stack_gcd.pop(-1)
                    stack_gcd.append(math.lcm(top,top2))                    
            stack_gcd.append(num)
        continue_flag=True
        while len(stack_gcd)>=2 and continue_flag:
            top=stack_gcd[-1]
            top2=stack_gcd[-2]
            if math.gcd(top,top2)==1:
                continue_flag=False 
            else:
                stack_gcd.pop(-1)
                stack_gcd.pop(-1)
                stack_gcd.append(math.lcm(top,top2))  
        return stack_gcd
if __name__=="__main__":
    solution=Solution()
    solution.replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825])