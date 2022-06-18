from collections import defaultdict
from typing import List 
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_index_dict=defaultdict(list)
        for index,num in enumerate(nums):
            num_index_dict[num].append(index)
        ans=0
        for num,num_index_list in num_index_dict.items():
            for i in range(len(num_index_list)):
                for j in range(i+1,len(num_index_list)):
                    if (num_index_list[i]*num_index_list[j])%k==0:
                        ans+=1 
        return ans 
if __name__=="__main__":
    solution=Solution()
    solution.countPairs(nums = [3,1,2,2,2,1,3], k = 2)