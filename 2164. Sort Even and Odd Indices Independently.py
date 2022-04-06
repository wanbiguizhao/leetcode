from collections import Counter
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums)<=2:
            return nums 
        even_index_counter=Counter([num for num in nums[::2]])
        odd_index_counter=Counter([num for num in nums[1::2]])
        
        even_index=0
        for i in range(101):
            num_count=even_index_counter[i]
            while num_count>0:
                nums[even_index]=i
                even_index+=2
                num_count-=1
        odd_index=1
        for i in reversed(range(101)):
            num_count=odd_index_counter[i]
            while num_count>0:
                nums[odd_index]=i
                odd_index+=2
                num_count-=1
        return nums