from typing import  List
class Solution:
    def longestConsecutive_1(self, nums: List[int]) -> int:
        ans=0
        dict_suffix_len={num:1 for num in nums}
        for num in nums:
            if dict_suffix_len[num]==1: 
                next_num=num+1 
                while next_num in dict_suffix_len and dict_suffix_len[next_num]==1:
                     next_num+=1
                base=0
                # 一种情况是next_num not in dict_suffix_len 
                # 另一种情况是next_num  in dict_suffix_len 
                if next_num in dict_suffix_len:
                    base=dict_suffix_len[next_num]
                next_num=next_num-1 # dict_suffix_len 中增加不必要的数字
                base+=1
                while next_num>=num:
                    dict_suffix_len[next_num]=base
                    base+=1
                    next_num-=1
            ans=max(dict_suffix_len[num],ans)
        return ans 
    def longestConsecutive(self, nums: List[int]) -> int:
        # 通过集合，先找到nums中连续区域最小的区域。

            
                        
if __name__ == "__main__":
    instance=Solution()
    instance.longestConsecutive(nums = [100,4,200,1,3,2])
    instance.longestConsecutive(nums= [0,3,7,2,5,8,4,6,0,1])
