from random import sample, randint,choice
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
        
from random import choice
class RandomizedSet():
    """

    官方答案，
    0. 字典加数组的方案，解决查询问题。
    1. choice用的好，解决随机问题。
    2. 最后一个数字覆盖被删除的字，解决删除o(1)问题。
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)