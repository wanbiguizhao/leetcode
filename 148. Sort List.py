# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next
class Solution:
    def sortList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 归并排序：两个指针进行排序。
        # 突破点是找到1/2的节点的指针。
        if not head:
            return None 
        
        pre_p_one_step=None
        p_one_step=head
        p_two_step=head.next
        while p_one_step and p_two_step:
            pre_p_one_step=p_one_step
            p_one_step=p_one_step.next
            p_two_step=p_two_step.next
            if not p_two_step:
                break
            p_two_step.next=p_two_step.next
        if p_one_step==head:
            # 当前只剩下一个节点了
            return head

        pre_p_one_step.next=None# 拆分成两个独立的链表
        helper_head=ListNode()
        helper_head.next=None 
        tail_node=helper_head
        one_node=self.sortList(head)# 
        two_node=self.sortList(p_one_step)#
        while one_node and two_node:
            tmp_node=None
            if one_node.val< two_node.val:
                tmp_node=one_node
                one_node=one_node.next
                tail_node.next=tmp_node
                tail_node=tmp_node
            else:
                tmp_node=two_node
                two_node=two_node.next 
                tail_node.next=tmp_node
                tail_node=tmp_node
            tmp_node.next=None

        if one_node:
            tmp_node.next=one_node
        if two_node:
            tmp_node.next=two_node
        return helper_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 归并排序：两个指针进行排序。
        # 不能使用递归的方法，只能使用逐步增长步长的方法。
        if not head:
            return None 
        
        pre_p_one_step=None
        p_one_step=head
        p_two_step=head.next
        while p_one_step and p_two_step:
            pre_p_one_step=p_one_step
            p_one_step=p_one_step.next
            p_two_step=p_two_step.next
            if not p_two_step:
                break
            p_two_step.next=p_two_step.next
        if p_one_step==head:
            # 当前只剩下一个节点了
            return head

        pre_p_one_step.next=None# 拆分成两个独立的链表
        helper_head=ListNode()
        helper_head.next=None 
        tail_node=helper_head
        one_node=self.sortList(head)# 
        two_node=self.sortList(p_one_step)#
        while one_node and two_node:
            tmp_node=None
            if one_node.val< two_node.val:
                tmp_node=one_node
                one_node=one_node.next
                tail_node.next=tmp_node
                tail_node=tmp_node
            else:
                tmp_node=two_node
                two_node=two_node.next 
                tail_node.next=tmp_node
                tail_node=tmp_node
            tmp_node.next=None

        if one_node:
            tmp_node.next=one_node
        if two_node:
            tmp_node.next=two_node
        return helper_head.next


        