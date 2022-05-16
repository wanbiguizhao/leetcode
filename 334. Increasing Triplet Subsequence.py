from typing import List

from sklearn import tree,
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp=[] # 使用三个空间复杂度的代码
        for num in nums:
            if not dp :
                dp.append(num)
            elif len(dp)==1:
                if num< dp [0]:
                    dp[0]=num 
                elif num>dp[0]:
                    dp.append(num)
            elif len(dp)==2:
                if num<dp[0]:
                    dp[0]=num 
                elif num<dp[1] and num>dp[0]:
                    dp[1]=num 
                elif num>dp[1]:
                    dp.append(num)
                    return True 
        return False 
            
                