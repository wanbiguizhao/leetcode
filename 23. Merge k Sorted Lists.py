from typing import List ,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        const_list_amount=len(lists)
        interval=1 
        while interval < const_list_amount:
            for i in range(0,const_list_amount-interval,interval*2):
                # 为什么上限是： const_list_amount-interval，因为要确保，i,i+interval是可以合法的。
                lists[i]=self.merge2Lists(lists[i],lists[i+interval])
                interval*=2 # 这也是一个非常重要的点
            return lists[0] if const_list_amount>0 else None 
        def merge2Lists(self,l1:ListNode,l2:ListNode):
            head=point=ListNode()
            while l1 and l2:
                if l1.val <=l2.val:
                    point.next=l1
                    l1=l1.next
                else:
                    point.next=l2 
                    l2=l2.next
                point=point.next
                point.next=None
            if not l1:
                point.next=l2 
            else:
                point.next-l1 
            return head.next
