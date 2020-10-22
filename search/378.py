
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left=matrix[0][0]
        right=matrix[-1][-1]
        while left<right:
            mid=(left+right)//2
            cnt=0
            for row in matrix:
                cnt+=upper_bound(row,mid)
            if cnt<k:
                left=mid+1
            else:
                right=mid
        return left
                
    
    
def upper_bound( nums ,target):
    """
    非递减数组中，返回第一个大于target的值的位置
    """
    low,high=0,len(nums)-1
    pos=len(nums)
    while low<high:
        mid=(low+high)//2
        print(low,high,mid)
        if nums[mid]<=target:
            low=mid+1
        else:
            high=mid
            pos=high
    if nums[low]>target:
        pos=low
    return pos

s=Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
    ]
k = 8
print(s.kthSmallest(matrix,k))
