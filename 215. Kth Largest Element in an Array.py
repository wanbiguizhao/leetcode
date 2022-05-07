from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 是否存在重复数字的情况？
        # 堆排序，使用堆排序
        # 堆排序维持一个长度为k的堆，O(Nlogk)的时间复杂度，K的空间复杂度。
        """
        Runtime: 72 ms, faster than 80.16% of Python3 online submissions for Kth Largest Element in an Array.
        Memory Usage: 14.8 MB, less than 75.13% of Python3 online submissions for Kth Largest Element in an Array.
        使用库函数排序，速度非常的快！
        """
        nums.sort()
        return nums[-k]
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 使用快排
        """
        Runtime: 3159 ms, faster than 5.01% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.8 MB, less than 43.18% of Python3 online submissions for Kth Largest Element in an Array.
Next challenges:
        """
        def quikselect(left,right):
            pivot=nums[left] 
            l=left + 1 
            r=right
            while l<=r:
                if nums[l]< pivot and nums[r]> pivot:
                    nums[l],nums[r]=nums[r],nums[l]
                    l+=1
                    r-=1
                if nums[l]>=pivot:
                    l+=1
                if nums[r]<=pivot:
                    r-=1
            nums[left],nums[r]=nums[r],nums[left]
            return r
        left=0 
        right=len(nums)
        while True:
            pos = quikselect(left,right)
            if pos==k-1 :
                return nums[pos]
            elif pos>k-1:
                right=pos-1
            else:
                left=pos+1
