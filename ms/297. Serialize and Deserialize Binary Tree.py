
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return "" 
        
        levelQueue=[(0,root)]
        ans=""
        while levelQueue :
            tmpQueue=[]
            for nodeInfo in levelQueue:
                nodeIndex, nodeObject=nodeInfo[0],nodeInfo[1]
                ans+="{}->{};".format(nodeIndex,nodeObject.val)
                if nodeObject.left:
                    leftSonIndex=nodeIndex*2+1
                    tmpQueue.append([leftSonIndex,nodeObject.left])
                if nodeObject.right:
                    rightSonIndex=nodeIndex*2+2
                    tmpQueue.append([rightSonIndex,nodeObject.right])
            levelQueue=tmpQueue
            #print(ans)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodeInfoList=data.split(";")
        nodeCache={}
        for nodeInfo in nodeInfoList[:-1]:
            nodeIndex,nodeVal=nodeInfo.split("->")
            nodeCache[int(nodeIndex)]=TreeNode(int(nodeVal))
        #print(nodeCache)
        rootnode=TreeNode(nodeCache[0].val)
        levelQueueNodeAndIndex=[]
        if 1 in nodeCache:
            rootnode.left=nodeCache[1]
            levelQueueNodeAndIndex.append(1)
        if  2 in nodeCache:
            rootnode.right=nodeCache[2]
            levelQueueNodeAndIndex.append(2)
        while levelQueueNodeAndIndex:
            tmpQueue=[]
            #print(levelQueueNodeAndIndex)
            for nodeIndex in levelQueueNodeAndIndex:
                treenode=nodeCache[nodeIndex]
                leftSonIndex=nodeIndex*2+1
                if leftSonIndex in nodeCache:
                    tmpQueue.append(leftSonIndex)
                    treenode.left=nodeCache[leftSonIndex]
                rightSonIndex=nodeIndex*2+2
                if rightSonIndex in nodeCache:
                    tmpQueue.append(rightSonIndex)
                    treenode.right=nodeCache[rightSonIndex]
            levelQueueNodeAndIndex=tmpQueue
            #print(tmpQueue)
        return rootnode