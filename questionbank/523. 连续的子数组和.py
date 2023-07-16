"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum=[0]*(len(nums)+1)
        hash_mode_k={}
        for i in range(1,len(presum)):
            presum[i]=nums[i-1]+presum[i-1]
        print(presum)
        for i in range(0,len(presum)):
            mode_k=presum[i]%k
            if mode_k in hash_mode_k:
                if hash_mode_k[mode_k]+1<i:
                    return True
            else:
                hash_mode_k[mode_k]=i  
        return False
            
            
                