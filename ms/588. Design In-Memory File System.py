from typing import List 
class FileSystem:
    # 使用字典进行建模吧
    """_summary_
    {
        "name":"",
        "content":"",
        "children":{},
        "isdDir":"true"
    }
    Runtime: 126 ms, faster than 7.27% of Python3 online submissions for Design In-Memory File System.
    Memory Usage: 14.6 MB, less than 22.30% of Python3 online submissions for Design In-Memory File System.
    """
    def __init__(self):
        self.root={
                "name":"",
                "content":"",
                "children":{},
                "isdDir":True
        } 
        

    def ls(self, path: str) -> List[str]:
        currentDir=self.root
        if path!="/":
            subPathList=path.split("/")
            for onePath in subPathList[1:]:
                currentDir=currentDir["children"][onePath]
            if currentDir["isdDir"]:
                return sorted(currentDir["children"].keys())
            return [currentDir["name"]]
        return sorted(currentDir["children"].keys())

    def mkdir(self, path: str) -> None:
        currentDir=self.root
        subPathList=path.split("/")
        for onePath in subPathList[1:]:
            if onePath  not in currentDir["children"]:
                currentDir["children"][onePath]={
                "name":onePath,
                "content":"",
                "children":{},
                "isdDir":True
                }
            currentDir=currentDir["children"][onePath]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        subPathList=filePath.split("/")
        currentDir=self.root
        for onePath in subPathList[1:]:
            if onePath not in currentDir["children"]:
                currentDir["children"][onePath]={
                "name":onePath,
                "content":"",
                "children":{},
                "isdDir":True
                }
            currentDir=currentDir["children"][onePath]
        if currentDir["isdDir"]:
            currentDir["isdDir"]=False 
        currentDir["content"]+=content

        

    def readContentFromFile(self, filePath: str) -> str:
        subPathList=filePath.split("/")
        currentDir=self.root
        for onePath in subPathList[1:]:
            currentDir=currentDir["children"][onePath]
        return currentDir["content"]

def testCase0(instance:FileSystem=FileSystem()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")
    instance.ls("/")
    instance.mkdir("/a/b")
    instance.addContentToFile("/a/b/c","a-b-c")
    res=instance.readContentFromFile("/a/b/c")
    instance.addContentToFile("/a/b/d","a-b-c")
    print(res,res=="a-b-c")
    res=instance.ls("/a/b/c")
    print(res,res==["c"])
    res=instance.ls("/a/b")
    print(res,res==["c","d"])
if __name__ =="__main__":
    #testCase0()
    #testCase0()
    testCase0()

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)