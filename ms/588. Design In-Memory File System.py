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
    """
    def __init__(self):
        self.root={
                "name":"",
                "content":"",
                "children":{},
                "isdDir":True
        } 
        

    def ls(self, path: str) -> List[str]:
        if path=="/":
            return []
        subPathList=path.split("/")
        currentDir=self.root
        for onePath in subPathList:
            currentDir=currentDir["children"][onePath]
        if currentDir["isdDir"]:
            return sorted(currentDir["children"].keys())
        return [currentDir["name"]]

    def mkdir(self, path: str) -> None:
        subPathList=path.split("/")
        currentDir=self.root
        for onePath in subPathList:
            if onePath  in currentDir["children"]:
                currentDir=currentDir["children"][onePath]
            else:
                currentDir[onePath]["children"]={
                "name":onePath,
                "content":"",
                "children":{},
                "isdDir":True
            }

    def addContentToFile(self, filePath: str, content: str) -> None:
        subPathList=filePath.split("/")
        currentDir=self.root
        for onePath in subPathList:
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
        for onePath in subPathList:
            currentDir=currentDir["children"][onePath]
        return currentDir["content"]

def testCase0(instance:FileSystem=FileSystem()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")
    instance.ls("/")
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