# Definition for singly-linked list.
from tkinter.tix import Tree
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head,tail):
            helpNode=ListNode()
            curNode=head 
            endNode=tail.next
            
            while curNode!=endNode:
                regHNext=helpNode.next 
                regCNext=curNode.next 

                helpNode.next = curNode
                curNode.next=regHNext

                curNode=regCNext
            return tail,head  
            
        if not head:
            return None 
        preheadNode=ListNode()
        preheadNode.next=head
        prev=preheadNode 

        begNode=head 
        endNode=head

        nextNode=head
        while True :
            x=1 
            while x<=k and nextNode:
                x+=1
                endNode=nextNode
                nextNode=nextNode.next
            if x<=k:
                break
            else:
                newHead,newEnd=reverse(begNode,endNode)
                preNode.next=newHead
                newEnd.next=nextNode

                preNode=newEnd
                begNode=nextNode
                endNode=nextNode
        return preheadNode.next 