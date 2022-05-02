from curses import noecho


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList_1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_maping_hash={}
        copy_head=Node(-1)
        origin_pointer=head 
        cp_pointer=copy_head
        while origin_pointer!=None:
            cp_pointer.next=Node(origin_pointer.val)
            cp_pointer=cp_pointer.next
            node_maping_hash[origin_pointer]=cp_pointer # 实现random指针定位
            origin_pointer=origin_pointer.next
        origin_pointer=head 
        cp_pointer=copy_head.next
        while origin_pointer!=None: # 空值检查
            random_node=origin_pointer.random
            cp_random_node=None
            if  random_node:
                cp_random_node=node_maping_hash[random_node]
            cp_pointer.random=cp_random_node

            cp_pointer=cp_pointer.next
            origin_pointer=origin_pointer.next

        return copy_head.next
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # one pass 
        def get_clone_node(node):
            if not node:
                return None
            if node in node_maping_hash:
                return node_maping_hash[node]
            cp_node=Node(node.val)
            node_maping_hash[node]=cp_node
            return cp_node
        node_maping_hash={}
        copy_head=Node(-1)
        origin_pointer=head 
        cp_pointer=copy_head
        while origin_pointer!=None:

            cp_pointer.next=get_clone_node(origin_pointer)
            cp_pointer=cp_pointer.next
            cp_pointer.random=get_clone_node(origin_pointer.random)
            origin_pointer=origin_pointer.next
        return copy_head.next
