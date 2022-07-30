import re


class MinStack:
    # Q1 what is happening when methods pop,top and getMin operations will always be called on non-empty stacks?
    # Q2 
    def __init__(self):
        self.data=[]


    def push(self, val: int) -> None:
        if len(self.data)==0:
            self.data.append((val,val))
        else :
            self.data.append((val,min(self.data[-1][-1],val)))


    def pop(self) -> None:
        val=self.data[-1][0]
        self.data.pop(-1)
        return val  


    def top(self) -> int:
        val=self.data[-1][0]
        return val


    def getMin(self) -> int:
        val=self.data[-1][1]
        return val