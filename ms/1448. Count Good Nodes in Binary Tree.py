# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preOrderNode(root:TreeNode,currentPathMaxNodeValue):
            if not root:
                return 
            if root.val>=currentPathMaxNodeValue:
                self.ans+=1
                currentPathMaxNodeValue=root.val
            preOrderNode(root.left,currentPathMaxNodeValue)
            preOrderNode(root.right,currentPathMaxNodeValue)

        self.ans=0
        preOrderNode(root,root.val)

        return self.ans


            

def testCase0(instance:Solution=Solution()):
    pass 



def wrongCase0(instance:Solution=Solution()):
    pass 




if __name__ =="__main__":
    
    testCase0()
    wrongCase0()