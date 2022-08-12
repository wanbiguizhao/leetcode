import queue
from turtle import right
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans=[]
        if not root:
            return ans 
        
        levelQueue=[(0,root)]
        ans=""
        stop_flag=False
        while levelQueue and not stop_flag:
            tmpQueue=[]
            for nodeInfo in levelQueue:
                nodeIndex, nodeObject=nodeInfo[0],nodeInfo[1]
                ans+="{}->{};".format(nodeIndex,nodeObject.val)
                if nodeObject.left:
                    leftSonIndex=nodeIndex*2+1
                    tmpQueue.append([leftSonIndex,nodeObject])
                if nodeObject.right:
                    rightSonIndex=nodeIndex*2+2
                    tmpQueue.append([rightSonIndex,nodeObject])
            levelQueue=tmpQueue
        print(ans)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodeInfoList=data.spilt(";")
        nodeCache={}
        for nodeInfo in nodeInfoList:
            nodeIndex,nodeVal=nodeInfo.split("->")
            nodeCache[nodeIndex]=int(nodeVal)

        rootnode=TreeNode(data['0'])
        levelQueueNodeAndIndex=[[rootnode,0]] 
        index=0

        while levelQueueNodeAndIndex:
            tmpQueue=[]
            for data in levelQueueNodeAndIndex:
                index,treeNode=data[0],data[1]
                if treeNode==None:
                    continue 
                else:
                    leftSonIndex=index*2+1
                    if data[leftSonIndex]:
                        leftTreeNode = TreeNode(data[leftSonIndex])
                        treeNode.left= leftTreeNode 
                        tmpQueue.append([leftSonIndex,leftTreeNode])
                    rightSonIndex=index*2+2
                    if data[rightSonIndex]:
                        rightTreeNode = TreeNode(data[rightSonIndex])
                        treeNode.right=rightTreeNode
                        tmpQueue.append([rightSonIndex,rightTreeNode])
            levelQueueNodeAndIndex=tmpQueue
        return rootnode

        