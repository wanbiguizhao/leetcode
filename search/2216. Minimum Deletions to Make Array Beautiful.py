from pickletools import read_uint1
from tkinter.tix import Tree
from typing import List 
# 需要使用贪心算法
class Solution_dfs:
    # 超时，只能只用bfs。
    def minDeletion(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0 
        self.ans=len(nums)
        self._min_deletion(nums,0)
        return self.ans 
    
    def _min_deletion(self,nums:list[int],del_nums:int):
        if self.ans <= del_nums:
            return 
        def check_perfect_nums(nums):
            for index in range(0,len(nums),2):
                if nums[index]==nums[index+1]:
                    return False 
            return True 
        if len(nums)%2 == 0:
            if check_perfect_nums(nums):
                self.ans=del_nums
                return  
        
        for index,data in enumerate(nums):
            # delete one elements 
            self._min_deletion(nums[0:index]+nums[index+1:],del_nums+1) 
        
class Solution_bfs:
    # 超时，只能只用bfs。
    def minDeletion(self, nums: List[int]) -> int:
        def check_perfect_nums(nums):
            if len(nums)%2 !=0 :
                return False
            for index in range(0,len(nums),2):
                if nums[index]==nums[index+1]:
                    return False 
            return True 
        if len(nums)==0:
            return 0 
        self.ans=len(nums)
        bfs_cand_list=[nums]
        while bfs_cand_list:
            new_bfs_cand_list=[]
            new_bsf_cache=set()
            for cand_nums in bfs_cand_list:
                if check_perfect_nums(cand_nums):
                    return len(nums)-len(cand_nums)
                for index,data in enumerate(cand_nums):
                    new_cand=cand_nums[0:index]+cand_nums[index+1:]
                    str_cache="-".join(map(str,new_cand))
                    if str_cache not in new_bsf_cache:
                        new_bsf_cache.add(str_cache)
                        new_bfs_cand_list.append(cand_nums[0:index]+cand_nums[index+1:])  
            bfs_cand_list=new_bfs_cand_list           

        return len(nums)
    
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        if not len(nums):
            return 0 
        from_even_index_flag=True
        count=0
        for index, num_value in  enumerate(nums):
            if from_even_index_flag and index%2==0:
                if  index  <len(nums)-1  and nums[index]==nums[index+1]:
                    count+=1
                    from_even_index_flag=False # 表示
            elif not from_even_index_flag and index%2==1:
                if index  < len(nums)-1 and nums[index]== nums[index+1]:
                    count+=1
                    from_even_index_flag=True 
        return count if (len(nums)-count)%2==0 else count+1 




if __name__ == "__main__":
    instance = Solution()
    print(instance.minDeletion([0,1,5,4,2,4,7,2,3,0,3,0,0,9,7,5,9,4,3,9,9,2,1,6,3,1,0,7,6,6,6,0,1,7,1,9,4,9,3,3,4,5,0,3,8,7,1,8,4,5]))