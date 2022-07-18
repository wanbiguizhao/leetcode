from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 对于进位的处理
    # 辅助节点的设立
    # l1 和 l2 的长度怎么样？
    # 链表有leading zero 的情况吗？ 
    # val的值的范围是多少？
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_flag=0 
        ans_node=ListNode(val=0,next=None)
        l3=ans_node
        while l1 and l2 :
            l3.next=ListNode(0)
            l3=l3.next
            xval=l1.val+l2.val+carry_flag
            l3.val=xval%10
            if xval>9:
                carry_flag=1
            else:
                carry_flag=0 
            l1=l1.next
            l2=l2.next
        while l1:
            l3.next=ListNode(0)
            l3=l3.next
            xval=l1.val+carry_flag
            l3.val=xval%10
            if xval>9:
                carry_flag=1
            else:
                carry_flag=0 
            l1=l1.next
        while l2:
            l3.next=ListNode(0)
            l3=l3.next
            xval=l2.val+carry_flag
            l3.val=xval%10
            if xval>9:
                carry_flag=1
            else:
                carry_flag=0 
            l2=l2.next
        if carry_flag>0:
            l3.next=ListNode(1)
        return ans_node.next 
def helpListnode(xList):
    headnode=ListNode()
    pnode=headnode
    for x in xList:
        pnode.next=ListNode(val=x)
        pnode =pnode.next
    return headnode.next
def printlist(node):
    ans=[]
    while node:
        ans.append(node.val)
        node=node.next
    print(ans)

def testCase0(instance:Solution=Solution()):
    # res=instance.reverseWords("    ")
    l1=helpListnode([1,8,8])
    l2=helpListnode([9,1,1])
    xnode=instance.addTwoNumbers(l1,l2)
    printlist(xnode)
    l1=helpListnode([1,8,8,9])
    l2=helpListnode([9,1,1])
    xnode=instance.addTwoNumbers(l1,l2)
    printlist(xnode)
    l1=helpListnode([1])
    l2=helpListnode([9])
    xnode=instance.addTwoNumbers(l1,l2)
    printlist(xnode)
    l1=helpListnode([0])
    l2=helpListnode([9])
    xnode=instance.addTwoNumbers(l1,l2)
    printlist(xnode)
if __name__ =="__main__":
    #testCase0()
    #testCase0()
    testCase0()