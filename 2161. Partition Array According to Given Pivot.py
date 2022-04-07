class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        new_nums=[pivot]*len(nums)
        pivot_list=[]
        pre_pivot=[]
        post_pivot=[]
        for num in nums:
            if num<pivot:
                pre_pivot.append(num)
            elif num>pivot:
                post_pivot.append(num)             
            else:
                pivot_list.append(num)
        return pre_pivot+pivot_list+post_pivot
            
    def pivotArray_bad(self, nums: List[int], pivot: int) -> List[int]:
        new_nums=[pivot]*len(nums)
        index=0
        for num in nums:
            if num<pivot:
                new_nums[index]=num
                index+=1
        index=len(nums)-1
        for num in nums[::-1]:
            if num>pivot:
                new_nums[index]=num
                index-=1
        return new_nums
                    