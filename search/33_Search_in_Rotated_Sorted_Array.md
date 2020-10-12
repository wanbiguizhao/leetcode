# 理解
典型的二分搜索问题。
目前了解的基本情况：
1. 数组是降序存储。

思路：
1. 先判断有序区间在mid的左侧还是右侧。(有一个注意点，就是mid坐标下取整的问题，会导致判断nums[right]>nums[mid] 和 nums[left]<nums[mid] 究竟表示左侧是连续的还是右侧是连续的有细微的差异。)
2. 确认好连续区间之后.
3. 判断target是否在连续区间，在的话正常搜索。
4. 判断target不在连续区间，转化成子问题（把所有空间放到mid的另一侧）进行搜索。


```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1 
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid 
            if nums[right]>nums[mid]:
                if nums[mid]<target and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[left]<=target and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return -1 
```

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1 
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left+1)//2
            if nums[mid]==target:
                return mid 
            if nums[mid]>nums[left]:
                if nums[left]<=target and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return -1 
```
