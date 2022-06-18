from typing import List 
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            ans=mapping[num%10]
            power=0
            if num==0:
                return ans 
            ans=0
            while num>0:
                ans=mapping[num%10]*10**power+ans
                num=num//10
                power+=1
            return ans 
        print(list(map(convert,nums)))
        return sorted(nums ,key=lambda x: convert(x))

if __name__=="__main__":
    solution=Solution()
    solution.sortJumbled([9,8,7,6,5,4,3,2,1,0],[0,9,8,7,6,5,4,3,2,1])  
            