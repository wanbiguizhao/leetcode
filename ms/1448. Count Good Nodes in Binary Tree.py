# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans=0
        pathMaxNodeValue=root.val 
        def preOrderNode(root:TreeNode,pathMaxNodeValue):
            if not root:
                return 
            if root.val>=pathMaxNodeValue:
                self.ans+=1 
            

def testCase0(instance:Solution=Solution()):
    pass 



def wrongCase0(instance:Solution=Solution()):
    pass 




if __name__ =="__main__":
    
    testCase0()
    wrongCase0()