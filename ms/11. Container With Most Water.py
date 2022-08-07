from typing import List 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftIndex,rightIndex=0,len(height)-1
        ans=0
        while leftIndex<rightIndex:
            hl,hr=height[leftIndex],height[rightIndex]
            
            if hl>hr:
                ans=max(ans,hr*(rightIndex-leftIndex))
                rightIndex-=1
            else:
                ans=max(ans,hl*(rightIndex-leftIndex))
                leftIndex+=1 
        return ans 

def testCase0(instance:Solution=Solution()):
    assert instance.maxArea(height = [1,8,6,2,5,4,8,3,7])==49
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()
