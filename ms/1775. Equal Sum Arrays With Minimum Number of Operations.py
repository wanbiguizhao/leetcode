from typing import List 
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Runtime: 2590 ms, faster than 8.70% of Python3 online submissions for Equal Sum Arrays With Minimum Number of Operations.
        Memory Usage: 18.2 MB, less than 79.85% of Python3 online submissions for Equal Sum Arrays With Minimum Number of Operations.
        算法有点类似
        """
        min_s1,max_s1=len(nums1),6*len(nums1)
        min_s2,max_s2=len(nums2),6*len(nums2)
        if min_s1>max_s2 or min_s2>max_s1:
            # 不可能有交际
            return -1 
        ans=0
        sums1=sum(nums1)
        sums2=sum(nums2)
        if sums2>sums1:
            nums1,nums2=nums2,nums1 # 交换，不影响原来的数值。
            sums1,sums2=sums2,sums1
        # sums1比较大，sums2比较小
        nums1.sort(reverse=True)
        nums2.sort() 
        ps2=0
        ps1=0
        distance=sums1-sums2
        while distance>0:
            if ps1<len(nums1) and ps2<len(nums2):
                # 这一步非常重要，贪心法，每次去一个最大的数值缩小distance
                # 双指针每次只移动一个距离。
                if nums1[ps1]-1 >6-nums2[ps2]:
                    distance-=nums1[ps1]-1
                    ps1+=1
                    ans+=1
                else:
                    distance-=6-nums2[ps2]
                    ps2+=1
                    ans+=1
                continue
                    

            if ps1<len(nums1):
                distance-=nums1[ps1]-1
                ps1+=1
                ans+=1
            if ps2<len(nums2):
                distance-=6-nums2[ps2]
                ps2+=1
                ans+=1
        return ans 
def testCase0(instance:Solution=Solution()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")
    # res=instance.minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2])
    # print(res,res==3)
    res=instance.minOperations(nums1 = [1,2,3,4,5,6], nums2 = [6,6,6,6,6,6])
    print(res,res==3)
    res=instance.minOperations(nums1 = [6], nums2 = [6,6,6,6,6,6])
    print(res,res==6)
    res=instance.minOperations(nums1 = [6], nums2 = [6,6,6,6,6,6,6])
    print(res,res==-1)
    res=instance.minOperations(nums1 = [1,2,3], nums2 = [3,2,1])
    print(res,res==0)

def wrong_testcase0(instance:Solution=Solution()):
    """_summary_

    Args:
        instance (Solution, optional): _description_. Defaults to Solution().

            if ps1<len(nums1):
                if nums1[ps1]> 1 :
                    ans+=1
                    sums1-=min(nums1[ps1]-1,sums1-sums2)
            ps1+=1
            if sums1!=sums2 and ps2<len(nums2):
                if nums2[ps2]<6:
                    ans+=1
                    sums2+=min(6-nums2[ps2],sums1-sums2)
            错误原因分析，究竟是应该先给s2加数值，还是先给s1减数值，是一个问题？
    """
    # res=instance.minOperations(nums1 =[5,2,1,5,2,2,2,2,4,3,3,5], nums2 = [1,4,5,5,6,3,1,3,3])
    # print(res,res==1)
    # res=instance.minOperations( 
    #         [1,2,3,4,5,6],
    #         [1,1,2,2,2,2])
    # print(res,res==3)
    res=instance.minOperations( 
[1,5,5,2,1,1,1,1,4,4,4,1,5,2,2,4,6,5,1,5,3,5,6,2,3,1,5,4,4,1,2,4,1,1,6,3,6,4,4,4,3,5,5,5,2,6,4,2,5,4,2,6,3,4,6,1,5,3,2,3,5,2,1,3,2,4,4,4,5,3,5,5,4,1,1,6,5,6,3,5,3,6,5,6,5,4,4,4,5,6,6,6,4,2,4,6,1,2,1,5,3,4,5,5,6,6,1,4,3,1,5,3,4,1,2,1,4,4,5,6,5,3,1,5,1,3,3,6,5,3,5,6,2,6,3,1,2,3,3,1,1,4,3,2,6,6,2,1,2,4,3,5,5,4,3,1,1,5,2,5,1,4,5,6,4,5,2,1,2,5,3,2,6,3,4,3,4,5,4,6,3,4,4,3,3,4,2,2,6,2,6,3,1,1,5,3,1,1,4,2,5,5,5,4,3,6,5,5,5,1,1,3,6,2,3,6,3,4,2,5,4,4,3,5,6,4,3,5,1,1,3,3,1,1,6,4,6,2,1,4,3,5,5]
,[1,2,5,4,3,3,5,1,1,6,2,5,4,4,5,6,6,4,2,5,6,2,3,4,5,2,4,4,3,6,6,5,4,1,2,1,2,3,3,2,6,1,1,1,1,3,5,6,2,1,1,1,4,6,5])
    print(res,res==184)
if __name__ =="__main__":
    #testCase0()
    #testCase0()
    wrong_testcase0()