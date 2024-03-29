from cmath import inf


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 数学公式计算，可以得出zig存在两个方向的变化。
        if numRows==1:
            return s 
        down_direction=[1,0]
        right_up_direction=[-1,1]
        directions=[]
        for i in range(numRows-1):
            directions.append(down_direction)
        for i in range(numRows-1):
            directions.append(right_up_direction)
        ansCoordinateList=[[0,0,s[0]]]
        directionIndex=0
        for x in s[1:]:
            direction=directions[directionIndex]
            info=ansCoordinateList[-1]
            ansCoordinateList.append([info[0]+direction[0],info[1]+direction[1],x ])
            directionIndex+=1
            directionIndex%=2*(numRows-1)
        ansCoordinateList.sort()
        return "".join([ info[-1] for info in ansCoordinateList])# 把字符串拼接起来

    def convert(self, s: str, numRows: int) -> str:
        # 数学公式计算，可以得出zig存在两个方向的变化。
        if numRows==1:
            return s 
        down_direction=[1,0]
        right_up_direction=[-1,1]
        directions=[]
        for i in range(numRows-1):
            directions.append(down_direction)
        for i in range(numRows-1):
            directions.append(right_up_direction)
        ans_cache={}
        ans_cache[0]=[s[0]]
        currentCoordinateX=0
        currentCoordinateY=0
        ansCoordinateList=[[0,0,s[0]]]
        directionIndex=0
        for x in s[1:]:
            direction=directions[directionIndex]
            currentCoordinateX=currentCoordinateX+direction[0]
            currentCoordinateY=currentCoordinateY+direction[1]
            if currentCoordinateX not in ans_cache:
                ans_cache[currentCoordinateX]=[]
            ans_cache[currentCoordinateX].append(x)
            directionIndex+=1
            directionIndex%=2*(numRows-1)
        ans=""
        for row in range(numRows):
            ans+="".join(ans_cache.get(row,""))# 注意异常值处理
        return ans
        
def testCase0(instance:Solution=Solution()):
    print(instance.convert("Abcd",2))
    print(instance.convert("Abcd",1))
    print(instance.convert(s = "PAYPALISHIRING", numRows = 4)=="PINALSIGYAHRPI")
    print(instance.convert(s = "PAYPALISHIRING", numRows = 3)=="PAHNAPLSIIGYIR")



def wrongCase0(instance:Solution=Solution()):
    print(instance.convert(s = "A", numRows = 2)=="A")




if __name__ =="__main__":
    
    testCase0()
    wrongCase0()