from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 先走n步，然后进行计算
        # 使用一个辅助节点比较容易计算。
        add_head=ListNode()
        add_head.next=head # 新增加一个辅助节点
        current_node=add_head

        while n>0 and current_node !=None:
            current_node=current_node.next
            n=n-1
        
        pre_n_node=add_head
        n_node=add_head
        
        while current_node != None:
            current_node=current_node.next
            pre_n_node=n_node
            n_node=n_node.next
        pre_n_node.next=n_node.next

        return add_head.next

        
        
        
