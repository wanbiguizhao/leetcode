class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_zero_node=head
        zero_node=head 
        data_node=head.next
        while data_node:
            if data_node.val!=0:
                zero_node.val+=data_node.val
                del_node=data_node
                data_node=data_node.next
                del del_node
            else:
                pre_zero_node=zero_node
                zero_node.next=data_node
                zero_node=data_node
                data_node=data_node.next
        pre_zero_node.next=None 
        del zero_node
        return head

            
        