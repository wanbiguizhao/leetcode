from typing import List 

class Solution:
    def trap(self, height: List[int]) -> int:
        # 心得，手工模拟一下处理流程就可以了，双指针，上一个的高度，当前高度。
        # 每一步计算增量的水的空间
        # 然后再计算占用的水的空间
        # 
        beg,end=0,len(height)-1
        ans=0
        preHeight=0
        incrementWater=0
        while beg<end:
            if height[beg]>=height[end]:
                currentHeight=height[end]
                incrementWater=-min(preHeight,currentHeight)
                if currentHeight> preHeight:
                    incrementWater+=(end-beg-1)*(currentHeight-preHeight)# 增量的水。
                    preHeight=currentHeight
                end-=1
            else:
                currentHeight=height[beg]
                incrementWater=-min(preHeight,currentHeight)
                if currentHeight> preHeight:
                    incrementWater+=(end-beg-1)*(currentHeight-preHeight)# 增量的水。
                    preHeight=currentHeight
                beg+=1 
            ans+=incrementWater 
        return ans 


def testCase0(instance:Solution=Solution()):
   assert instance.trap( height = [0,1,0,2,1,0,1,3,2,1,2,1])==6
   assert instance.trap(height = [4,2,0,3,2,5])==9
   assert instance.trap(height = [0,1,2,0,2,1])==2
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()