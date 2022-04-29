from typing import Optional ,List

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # 层次遍历，不满足空间复杂度要求。
        # 不是要求常量的空间复杂度，所以原来的层次遍历不可以使用了。
        # 注意，this is a perfect binary tree
        if not root:
            return root 
        if root.left and root.right:
            root.left.next=root.right
            self.connect(root.left)
            self.connect(root.right)
            from_node=root.left.right
            to_node=root.right.left
            while from_node and to_node:
                from_node.next=to_node
                from_node=from_node.right
                to_node=to_node.left
        return root 
            