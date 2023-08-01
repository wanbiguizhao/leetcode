class Solution:
    def searchRange(self,nums,target):
        l,r=0,len(nums)-1
        first,last=-1,-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                first=mid 
                r=mid-1 
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1 
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                last=mid 
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1 
        return first,last        
