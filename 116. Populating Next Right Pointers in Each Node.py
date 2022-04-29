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
        # 递归就可以了
        node_queue=[]
        ans=[]
        if not root:
            return []
        node_queue.append
        pass 