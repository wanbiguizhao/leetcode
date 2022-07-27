from typing import List 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums的长度是否会小于三的情况？
        # nums[i,j,k]是否有相同的情况
        # 思路
        # 排序，固定一个头，两边搜索。
        ans=[] 
        nums.sort()
        def binarySearch(beg,end,val):
            res=[]
            while beg<end:
                if nums[beg]+nums[end]==val:
                    res.append(
                        [-val,nums[beg],nums[end]]
                    )
                    beg=beg+1
                    while beg<constLenOfNums and nums[beg]==nums[beg-1]:
                        beg=beg+1
                    end=end-1
                    while end>=0 and nums[end]==nums[end+1]:
                        end=end-1
                elif nums[beg]+nums[end]>val:
                    end-=1 
                else:
                    beg+=1 
            return res  
        constLenOfNums=len(nums)
        for index in range(constLenOfNums):
            if index-1>=0 and nums[index]==nums[index-1]: 
                continue 
            res= binarySearch(index+1,constLenOfNums-1,-nums[index])
            if res:
                ans.extend(res) 
        return ans 


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums的长度是否会小于三的情况？
        # nums[i,j,k]是否有相同的情况
        # 思路
        # 排序，固定一个头，两边搜索。
        # 没有使用子函数
        ans=[] 
        nums.sort()
        constLenOfNums=len(nums)
        for index in range(constLenOfNums):
            if index-1>=0 and nums[index]==nums[index-1]: 
                continue 
            val=-nums[index]
            beg=index+1
            end=constLenOfNums-1
            while beg<end:
                if nums[beg]+nums[end]==val:
                    ans.append([-val,nums[beg],nums[end]])           
                    beg=beg+1
                    while beg<constLenOfNums and nums[beg]==nums[beg-1]:
                        beg=beg+1
                    end=end-1
                    while end>=0 and nums[end]==nums[end+1]:
                        end=end-1
                elif nums[beg]+nums[end]>val:
                    end-=1 
                else:
                    beg+=1 
        return ans 

             
def testCase0(instance:Solution=Solution()):
    res=instance.threeSum([0,0,0])
    print(res)
    res=instance.threeSum([0,0,0,-1,1,-1,1])
    print(res)
    res=instance.threeSum([0,0,0])
    print(res)
    res=instance.threeSum([-2,-3,5,1,2,0])
    print(res)


def wrongCase0(instance:Solution=Solution()):
    res=instance.threeSum([0,-2,1,1,2])
    print(res)


if __name__ =="__main__":
    
    testCase0()
    wrongCase0()