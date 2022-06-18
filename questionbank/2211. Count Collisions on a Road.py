import pysnooper
from typing import List
from copy import copy 
class Solution:
    @pysnooper.snoop()
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        def left_to_right_check():
            updateStatusFlag=False
            for index in range(len(directions)-1):
                if carStatusList[index]==0:
                    if directions[index]=="R":
                        if directions[index+1]=="S" or carStatusList[index+1]==1:
                            carStatusList[index]=1
                            updateStatusFlag=True
                        elif directions[index+1]=="L" and carStatusList[index+1]==0:
                            carStatusList[index]=1
                            carStatusList[index+1]=1
                            updateStatusFlag=True
                        else:
                            pass 
                    elif directions[index]=="S":
                        if directions[index+1]=="L" and carStatusList[index+1]==0:
                            carStatusList[index+1]=1
                            updateStatusFlag=True
                    else:
                        pass 
                else:
                    if  directions[index+1]=="L" and carStatusList[index+1]==0:
                        carStatusList[index+1]=1
            return updateStatusFlag
        def right_to_left_check():
            updateStatusFlag=False
            for index in range(len(directions)-1,0,-1):
                if carStatusList[index]==0:
                    if directions[index]=="L":
                        if directions[index-1]=="S" or carStatusList[index-1]==1:
                            carStatusList[index]=1
                            updateStatusFlag=True
                        elif directions[index-1]=="R" and carStatusList[index-1]==0:
                            carStatusList[index]=1
                            carStatusList[index-1]=1
                            updateStatusFlag=True
                        else:
                            pass 
                    elif directions[index]=="S":
                        if directions[index-1]=="R" and carStatusList[index-1]==0:
                            carStatusList[index-1]=1
                            updateStatusFlag=True
                    else:
                        pass 
                else:
                    if  directions[index-1]=="R" and carStatusList[index-1]==0:
                        carStatusList[index-1]=1
            return updateStatusFlag
        ans=0
        if len(directions)==1:
            return 0

        carStatusList=[0]*len(directions)
        updateStatusFlag=True 
        while updateStatusFlag:
            
            updateStatusFlag=left_to_right_check()
            updateStatusFlag=right_to_left_check()
            
        return sum(carStatusList)


if __name__=="__main__":
    instance=Solution()
    instance.countCollisions("RRRRRRS")
    instance.countCollisions("RRRRRRSLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"*20)
    pass             
        