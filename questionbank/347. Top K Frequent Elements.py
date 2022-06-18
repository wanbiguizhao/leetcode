from typing import List 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def get_right(target,left):
            # 找到 nums[i]> target 的最小i
            right=const_len
            while left<right:
                mid=(left+right)//2 
                if nums[mid]<=target:
                    left=mid+1
                else:
                    right=mid 
            return right 
        nums.sort()
        const_len=len(nums)
        ans_list=[]
        # 排序加二分查找；
        # 1. 计算nums[beg_index] 的最右侧的值。找到一个end，index
        # 2. 计算value 放入到一个 长度为2的堆栈中，
        beg_index=0
        while beg_index<const_len:
            end_index=get_right(nums[beg_index],beg_index)
            val=nums[beg_index]
            v_len=end_index-beg_index
            beg_index=end_index
            ans_list.append([v_len,val])
        ans_list.sort(reverse=True)
        #print([val for count,val in  ans_list[:k]])
        return [val for count,val in  ans_list[:k]]


if __name__ == "__main__":
    instance=Solution()
    instance.topKFrequent([1,2,3,2,3],2)
    instance.topKFrequent([1,2,3,2,3,4,4,4],1)