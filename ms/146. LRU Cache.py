from collections import defaultdict
class DataNode:
    def __init__(self,key=0,value=0) -> None:
        self.next:DataNode=None 
        self.pre:DataNode=None 
        self.value=value
        self.key=key
class LRUCache:
    # 双链表，哈希
    def __init__(self, capacity: int):
        self.nodeCache={}#defaultdict(DataNode)# key:node
        self.capacity=capacity
        self.len=0
        self.headNode=DataNode()
        self.headNode
        self.tailNode=DataNode()
        self.headNode.next,self.tailNode.pre=self.tailNode,self.headNode

    def get(self, key: int) -> int:
        if  self.nodeCache.get(key,None):
            node=self.nodeCache[key]

            # 调整缓存位置
            node.pre.next=node.next
            node.next.pre=node.pre 
            # node.pre=None 
            # node.next=None 
            node.next,node.pre=self.headNode.next,self.headNode
            self.headNode.next.pre=node 
            self.headNode.next=node 
            return node.value
        return None
         

    def put(self, key: int, value: int) -> None:
        if self.nodeCache.get(key,None):
            node=self.nodeCache[key]
            node.value=value 
            # 调整位置。
            node.pre.next=node.next
            node.next.pre=node.pre 
            # node.pre=None 
            # node.next=None 
            node.next,node.pre=self.headNode.next,self.headNode
            self.headNode.next.pre=node 
            self.headNode.next=node 
        else:
            node=DataNode(key,value)
            if self.len==self.capacity:
                # 删除一个节点。
                tailNode=self.tailNode.pre
                tailNode.pre.next=self.tailNode 
                self.tailNode.pre=tailNode.pre 
                del self.nodeCache[tailNode.key]
                del tailNode 
            else:
                self.len+=1 
            self.nodeCache[key]=node # 增加缓存
            self.headNode.next.pre=node
            node.next= self.headNode.next
            self.headNode.next,node.pre=node,self.headNode  

if __name__=="__main__":
    instance=LRUCache(2)
    instance.put(1,1)
    instance.put(2,2)
    instance.get(1)
    instance.put(3,3)
    instance.get(3)

        
