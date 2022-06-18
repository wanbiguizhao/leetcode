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
        # 归并排序：两个指针进行排序。
        # 不能使用递归的方法，只能使用逐步增长步长的方法。
        if not head or not head.next:
            return head 
        
        pre_p_one_step=None
        p_one_step=head
        p_two_step=head
        while   p_two_step and p_two_step.next:
            pre_p_one_step=p_one_step
            p_one_step=p_one_step.next
            p_two_step=p_two_step.next
            p_two_step.next=p_two_step.next
        pre_p_one_step.next=None# 拆分成两个独立的链表
        helper_head=ListNode()
        helper_head.next=None 
        tail_node=helper_head
        one_node=self.sortList(head)# 
        two_node=self.sortList(p_one_step)#
        while one_node and two_node:
            if one_node.val< two_node.val:                
                tail_node.next=one_node
                one_node=one_node.next
            else:
                tail_node.next=two_node
                two_node=two_node.next 
            tail_node=tail_node.next

        if one_node:
            tail_node.next=one_node
        if two_node:
            tail_node.next=two_node
        return helper_head.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 归并排序：两个指针进行排序。
        # 不能使用递归的方法，只能使用逐步增长步长的方法。
        def merge(l1,l2):
            headx=ListNode()
            p=headx
            while l1 and l2:
                if l1.val<l2.val:
                    p.next=l1
                    l1=l1.next
                else :
                    p.next=l2
                    l2=l2.next
                p=p.next
            if l1:
                p.next=l1
            if l2:
                p.next=l2
            return headx.next
        if not head or not head.next:
            return head 
        p_one_step=head
        p_two_step=head.next
        while p_two_step and p_two_step.next:
            p_one_step=p_one_step.next
            p_two_step=p_two_step.next 
            p_two_step=p_two_step.next
        mid=p_one_step.next
        p_one_step.next=None
        return merge(self.sortList(head),self.sortList(mid))

        




        