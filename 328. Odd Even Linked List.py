from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_odd=ListNode()# 奇数
        head_even=ListNode()#偶数
        p_odd=head_odd
        p_even=head_even
        p=head
        bin_flag=True
        while p:
            if bin_flag:
                p_odd.next=p
                p=p.next
                p_odd=p_odd.next
                p_odd.next=None 
                bin_flag=False
            else:
                p_even.next=p 
                p=p.next
                p_even=p_even.next
                p_even.next=None 
                bin_flag=True
        p_odd.next=head_even.next
        return head_odd.next

