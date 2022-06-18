from pickletools import read_uint1
from typing import List
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2==1:
            return []
        beg=0
        ans=[0]
        while  ans[-1] < finalSum:
            beg+=2
            ans.append(beg)
            finalSum-=beg 
        ans[-1]+=finalSum
        return ans[1:]
if __name__=="__main__":
    solution=Solution()
    solution.maximumEvenSplit(28)


