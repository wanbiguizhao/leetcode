# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List,Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 首先要问的第一个问题是升序还是降序。
        def mergeTwoLists(alist:ListNode,bList:ListNode):
            ph=headNode=ListNode()
            pa=alist
            pb=bList
            while pa and pb :
                if pa.val<pb.val:
                    ph.next=pa 
                    ph=pa
                    pa=pa.next 
                else:
                    ph.next=pb 
                    ph=pb 
                    pb=pb.next 
            while pa :
                ph.next=pa
                ph=pa  
                pa=pa.next 
            while pb:
                ph.next=pb 
                ph=pb 
                pb=pb.next 
            return headNode.next
        ansNode=None 
        for node in lists:
            ansNode=mergeTwoLists(ansNode,node)
        return ansNode
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(alist:ListNode,bList:ListNode):
            ph=headNode=ListNode()
            pa=alist
            pb=bList
            while pa and pb :
                if pa.val<pb.val:
                    ph.next=pa 
                    ph=pa
                    pa=pa.next 
                else:
                    ph.next=pb 
                    ph=pb 
                    pb=pb.next 
            while pa :
                ph.next=pa
                ph=pa  
                pa=pa.next 
            while pb:
                ph.next=pb 
                ph=pb 
                pb=pb.next 
            return headNode.next
        if not lists :
            return None
        beg,end=0,len(lists)-1
        if beg==end:
            return lists[0]
        mid=(beg+end)//2
    
        return mergeTwoLists(self.mergeKLists(lists[beg:mid+1]),self.mergeKLists(lists[mid+1:]))
        # 注意空的数据集