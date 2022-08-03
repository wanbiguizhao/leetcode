from typing import List 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthElement(k:int):
            index1,index2=0,0 
            while True:
                if index1==m:
                    return nums2[index2+k-1]
                if index2==n:
                    return nums1[index1+k-1]
                if k==1:
                    return min(nums1[index1],nums2[index2])
                nIndex1=min(index1+k//2-1,m-1)
                nIndex2=min(index2+k//2-1,n-1)
                pivot1,pivot2=nums1[nIndex1],nums2[nIndex2]
                if pivot1<=pivot2:
                    k-=nIndex1-index1+1
                    index1=nIndex1+1
                else:
                    k-=nIndex2-index2+1
                    index2=nIndex2+1
        m,n=len(nums1),len(nums2)
        totalLength=m+n 
        if totalLength%2==1:
            return findKthElement((totalLength+1)//2)
        return (findKthElement((totalLength)//2)+findKthElement((totalLength)//2+1))//2
def testCase0(instance:Solution=Solution()):
    assert instance.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])==2.0
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()