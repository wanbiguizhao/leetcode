class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       pass 

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       pass 

   def getList(self) ->' [NestedInteger]':
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       pass 
class NestedIterator:
    def __init__(self, nestedList:' [NestedInteger]'):
        def unnested(xlist:NestedInteger):
            if xlist.isInteger():
                return [xlist.getInteger()]
            ans=[]
            for x in xlist.getList():
                ans.extend(unnested(x))
            print(ans)
            return ans

        self.len=0
        self.point=0
        self.store=[]
        for nested in nestedList:
            self.store.extend(unnested(nested))
        #print(self.store)
        self.len=len(self.store)
    
    def next(self) -> int:
        p=self.point
        self.point+=1
        return self.store[p]
         
        
    
    def hasNext(self) -> bool:
        return self.len!=self.point