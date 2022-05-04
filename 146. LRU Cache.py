from typing import Optional
class LinkNode:
    def __init__(self,val=0,key=0, preNode: 'LinkNode'=None, nextNode:'LinkNode'=None) -> None:
        self.val=val
        self.key=key
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
        self.headNode.nextNode=self.tailNode
        self.tailNode.preNode=self.headNode
        

    def get(self, key: int) -> int:
        if key in self.hash_node:
            # print(self.currentCapacity)
            # print(self.tailNode.preNode.val)
            node=self.hash_node[key]
            # print(node.val,node.key,node.preNode,node.nextNode)

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
        else:
            newNode=LinkNode(val=value,key=key)
            self.hash_node[key]=newNode

            if self.currentCapacity>=self.capacity:
                # 删除队尾的节点。
                delNode=self.tailNode.preNode
                self.tailNode.preNode=delNode.preNode
                delNode.preNode.nextNode=self.tailNode
                del self.hash_node[delNode.key]
                del delNode
            else:
                self.currentCapacity+=1
            # insert new Node
            nextNode=self.headNode.nextNode
            nextNode.preNode=newNode
            newNode.nextNode=nextNode
            
            newNode.preNode=self.headNode
            self.headNode.nextNode=newNode
            






        