import pysnooper
from typing import List
from copy import copy 
class Solution:
    @pysnooper.snoop()
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.MAX_ROUND_NUM=len(aliceArrows)
        self.max_bob_points=-1
        self.max_bob_arrows=[]
        self.maximum(0,0,numArrows,aliceArrows,[0]*len(aliceArrows))
        return self.max_bob_arrows
    def maximum(self,round_counter:int,current_points:int,rest_num_arrows:int,aliceArrows:List[int],current_bob_arrows:List[int]):
        if round_counter > self.MAX_ROUND_NUM-1:
            if self.max_bob_points<current_points:
                self.max_bob_points=current_points
                self.max_bob_arrows=copy(current_bob_arrows)
                if rest_num_arrows>0:
                    self.max_bob_arrows[0]=rest_num_arrows+self.max_bob_arrows[0]
            return 
        if rest_num_arrows> aliceArrows[round_counter]:
            rest_num_arrows=rest_num_arrows-(aliceArrows[round_counter]+1)
            current_bob_arrows[round_counter]=aliceArrows[round_counter]+1
            self.maximum(round_counter+1,
                         current_points+round_counter,
                         rest_num_arrows,
                         aliceArrows,
                         current_bob_arrows)
            current_bob_arrows[round_counter]=0
            rest_num_arrows=rest_num_arrows+(aliceArrows[round_counter]+1)
        self.maximum(round_counter+1,current_points,rest_num_arrows,aliceArrows,current_bob_arrows)
        
            
if __name__=="__main__":
    instance=Solution()
    instance.maximumBobPoints(9,[1,1,0,1,0,0,2,1,0,1,2,0])
    pass             
        