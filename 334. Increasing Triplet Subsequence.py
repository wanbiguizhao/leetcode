from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp=[num] # 使用三个空间复杂度的代码

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
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp=[nums[0]] # 使用三个空间复杂度的代码
        # 深刻理解，扑克牌，每次把最小的放到合适位置的算法
        count=1
        for index in range(1,len(nums)):
            if dp[-1]<nums[index]:
                if count==2:
                    return True 
                else:
                    dp.append(nums[index])
                    count+=1
            elif dp[-1]>nums[index]:
                if count==2 : 
                    if nums[index]>dp[0] :
                        dp[-1]=nums[index]
                    elif nums[index]<dp[0]:
                        dp[0]=nums[index]
                else:
                    dp[-1]=nums[index]
        return False
            
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        i = float("inf")
        j = float("inf")
        
        for n in nums:
            
            if n <= i:
                i = n
                
            elif n <= j:
                j = n
                
            elif i != float("inf") and j != float("inf"):
                return True
            
        return False