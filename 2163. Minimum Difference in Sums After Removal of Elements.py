from typing import List
import heapq
from heapq import heapify,heapreplace

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # 三路法
        # 1-index, 从中间进行区分k，[1,k] 2n>k>=n 表示原来扣完n个数据的元素后,计算前n个有效元素的最后一个元素对应的是第k个坐标。
        # 此时[k+1,3n]的位置,肯定包含n个后面的数据，取n个最大的即可。
        # 转换成求前n个最大值，n个最小值了。
        # 有意思的定义变量left_index right_index 
        # 熟悉了 使用heapq 求topk
     
        const_s_len=len(nums)
        const_n=const_s_len//3
        left_min_list=[0]*const_s_len
        left_min_heapd=[]
        right_max_list=[0]*const_s_len
        right_max_heapd=[]
        for k in range(const_n):
            left_index=k
            heapq.heappush(left_min_heapd,-nums[left_index])
            right_index=const_s_len-k-1
            heapq.heappush(right_max_heapd,nums[right_index])
        right_max_list[const_s_len-const_n]=sum(right_max_heapd)
        left_min_list[const_n-1]=-sum(left_min_heapd)

        for k in range(const_n):
            left_index=k+const_n
            if -nums[left_index] > left_min_heapd[0]:
                left_min_list[left_index]=left_min_list[left_index-1]+left_min_heapd[0]+nums[left_index]
                heapq.heapreplace(left_min_heapd,-nums[left_index])
            else:
                left_min_list[left_index]=left_min_list[left_index-1]

            right_index= const_s_len-1-const_n-k
            if nums[right_index] > right_max_heapd[0]:
                right_max_list[right_index]=right_max_list[right_index+1]-right_max_heapd[0]+nums[right_index]
                heapq.heapreplace(right_max_heapd,nums[right_index])
            else:
                right_max_list[right_index]=right_max_list[right_index+1]
        ans=left_min_list[const_n-1]
        for k in range(const_n+1):
            index=k+const_n-1
            #print(index,left_min_list[index],right_max_list[index+1],left_min_list[index]-right_max_list[index+1])
            ans=min(ans,left_min_list[index]-right_max_list[index+1])
        return ans 
if __name__=="__main__":
    instance=Solution()
    print(instance.minimumDifference(nums = [3,1,2]))

    print(instance.minimumDifference(nums = [16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23]))
