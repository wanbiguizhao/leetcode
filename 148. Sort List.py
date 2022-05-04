# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 归并排序：两个指针进行排序。
        # 突破点是找到1/2的节点的指针。
        if not head:
            return None 
        helper_head=ListNode()
        helper_head.next=head
        pre_p_one_step=None
        p_one_step=helper_head
        p_two_step=head
        while p_one_step and p_two_step:
            pre_p_one_step=p_one_step
            p_one_step=p_one_step.next
            p_two_step=p_two_step.next
            if not p_two_step:
                break
            p_two_step.next=p_two_step.next
        if p_one_step==p_two_step:
            # 当前只剩下一个节点了
            return helper_head.next

        pre_p_one_step.next=None# 拆分成两个独立的链表
        helper
        one_node=self.sortList(head)# 
        two_node=self.sortList(p_one_step)#
        while one_node

        #half_node=head


        