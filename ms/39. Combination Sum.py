from typing import List 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def searchSum(endIndex,target,oneAns):
            if endIndex<0 or target<0:
                return
            if candidates[endIndex]==target:
                ansList.append(oneAns+[target])

            searchSum(endIndex,target-candidates[endIndex],oneAns+[ candidates[endIndex] ])
            searchSum(endIndex-1,target,oneAns)
            
        ansList=[]
        candidates.sort()
        searchSum(len(candidates)-1,target,[])
        return ansList


def testCase0(instance:Solution=Solution()):
    print(instance.combinationSum(candidates = [2,3,6,7], target = 7))
    print(instance.combinationSum(candidates = [2,3,5], target = 8))
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()