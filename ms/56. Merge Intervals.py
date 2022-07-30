from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans_list=[]
        intervals.sort()
        ans_list=[intervals[0]]
        cache={}
        for index in range(1,len(intervals)):
            ele=intervals[index]
            if ele[0]<=ans_list[-1][1]:
                ans_list[-1][1]=max(ele[1],ans_list[-1][1])
            else:
                ans_list.append(ele)
        return ans_list
def testCase0(instance:Solution=Solution()):
    print(instance.merge([[1,3],[2,6],[8,10],[15,18]]))



def wrongCase0(instance:Solution=Solution()):
    print(instance.merge([[1,15],[15,18]]))



if __name__ =="__main__":
    
    testCase0()
    wrongCase0()
