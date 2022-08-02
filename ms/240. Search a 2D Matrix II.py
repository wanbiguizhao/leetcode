from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 按照例子模拟一下程序就可以了。
        constRowLen=len(matrix)
        constColLen=len(matrix[0])
        ri,cj=constRowLen-1,0
        while ri>=0 and cj< constColLen:
            if matrix[ri][cj]> target:
                ri-=1
            elif matrix[ri][cj]<target:
                cj+=1
            else:
                return True 

        return False 
def testCase0(instance:Solution=Solution()):
    res=instance.searchMatrix( matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
    assert res==True
    res=instance.searchMatrix( matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 26)
    assert res==True
    res=instance.searchMatrix( matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 1)
    assert res==True
    res=instance.searchMatrix( matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 30)
    assert res==True
    res=instance.searchMatrix( matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = -1)
    assert res==False
    res=instance.searchMatrix( matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 31)
    assert res==False
    res=instance.searchMatrix( matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 8.5)
    assert res==False
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()