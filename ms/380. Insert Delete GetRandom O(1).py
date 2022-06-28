from random import sample, randint
class RandomizedSet:
    """
    Runtime: 1348 ms, faster than 5.00% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.3 MB, less than 56.61% of Python3 online submissions for Insert Delete GetRandom O(1).
    """
    def __init__(self):
        self.dataSet=set() 

    def insert(self, val: int) -> bool:
        if val in self.dataSet:
            return False 
        self.dataSet.add(val)
        return True 
        

    def remove(self, val: int) -> bool:
        if val in self.dataSet:
            self.dataSet.remove(val)
            return True 
        return False
        

    def getRandom(self) -> int:
        # 采用方法
        # 如何实现O(1)
        
        index=randint(0,len(self.dataSet)-1)
        i=0
        for x in self.dataSet:
            if i==index:
                break 
            i+=1

        return x
        #return sample(self.dataSet,1)[0]
        
