from tkinter.tix import Tree
from typing import List 
from collections import Counter
from xmlrpc.client import TRANSPORT_ERROR
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even_counter=Counter(nums[::2])
        odd_counter=Counter(nums[1::2])
        even_cnt_list=sorted([ [num_cnt,num ]  for num,num_cnt in  even_counter.items()],reverse=True)
        odd_cnt_list=sorted([ [num_cnt,num ]  for num,num_cnt in  odd_counter.items()],reverse=True)
        if even_cnt_list[0][1]!=odd_cnt_list[0][1]:
            return len(nums)-even_cnt_list[0][0]-odd_cnt_list[0][0]
        else:
            sec_even=0
            if len(even_cnt_list)>1:
                sec_even=even_cnt_list[1][0]
            sec_odd=0
            if len(odd_cnt_list)>1:
                sec_odd=odd_cnt_list[1][0]
            return len(nums)-max(even_cnt_list[0][0]+sec_odd,odd_cnt_list[0][0] + sec_even )

if __name__=="__main__":
    solution=Solution()
    # ans=solution.minimumOperations([1,1,1,1,1])
    # print(ans)
    # ans=solution.minimumOperations([1,1,1,1,1,1,1,0,1,1,2,3,2,4,2,5])
    # print(ans) 
    # ans=solution.minimumOperations([3,1,3,2,4,3])
    # print(ans)
    # ans=solution.minimumOperations([1,2,2,2,2])
    # print(ans)
    ans=solution.minimumOperations([69,91,47,74,75,94,22,100,43,50,82,47,40,51,90,27,98,85,47,14,55,82,52,9,65,90,86,45,52,52,95,40,85,3,46,77,16,59,32,22,41,87,89,78,59,78,34,26,71,9,82,68,80,74,100,6,10,53,84,80,7,87,3,82,26,26,14,37,26,58,96,73,41,2,79,43,56,74,30,71,6,100,72,93,83,40,28,79,24])
    print(ans)
        