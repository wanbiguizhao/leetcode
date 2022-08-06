from typing import List 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftIndex,rightIndex=0,len(height)-1
        ans=0
        while leftIndex<rightIndex:
            hl,hr=height[leftIndex],height[rightIndex]
            ans=max(ans,min(hl,hr)*(rightIndex-leftIndex))
            if hl>hr:
                rightIndex-=1
            else:
                leftIndex+=1 
        return ans 

def testCase0(instance:Solution=Solution()):
    assert instance.maxArea(height = [1,8,6,2,5,4,8,3,7])==49
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()
