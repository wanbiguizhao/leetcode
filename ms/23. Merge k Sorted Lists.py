# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List,Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 首先要问的第一个问题是升序还是降序。
        def mergeTwoLists(alist,bList):
            ph=headNode=ListNode()
            pa=alist
            pb=bList
            while pa and pb :
                
