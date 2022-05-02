from typing import Optional
class LinkNode:
    def __init__(self,val=0, preNode: 'LinkNode'=None, nextNode:'LinkNode'=None) -> None:
        self.val=val 
        self.preNode=preNode 
        self.nextNode=nextNode


class LRUCache:
    # hash索引加链表的方式

    def __init__(self, capacity: int):
        self.capacity=capacity 
        self.currentCapacity=0
        self.hash_node={}
        self.headNode=LinkNode()
        self.tailNode=LinkNode()
        
        

    def get(self, key: int) -> int:
        if key in self.hash_node:
            node=self.hash_node[key]

            # remove node
            preNode=node.preNode
            nextNode=node.nextNode
            
            preNode.nextNode=nextNode
            nextNode.preNode=preNode
            
            # insert node 
            self.headNode.nextNode.preNode=node
            node.nextNode=self.headNode.nextNode
            self.headNode.nextNode=node 
            node.preNode=self.headNode 
            return node.val
            
        return -1  

    def put(self, key: int, value: int) -> None:
        if key in self.hash_node:
            # set key 
            node=self.hash_node[key]
            node.val=value
        else:
            if self.currentCapacity>=self.capacity:
                # 删除队尾的节点。
                


        # remove node
        preNode=node.preNode
        nextNode=node.nextNode
        
        preNode.nextNode=nextNode
        nextNode.preNode=preNode
        
        # insert node 
        self.headNode.nextNode.preNode=node
        node.nextNode=self.headNode.nextNode
        self.headNode.nextNode=node 
        node.preNode=self.headNode 

        