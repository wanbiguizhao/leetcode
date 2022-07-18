from typing import List 
class TAGState:
    def __init__(self,context:"Solution",stack=[]) -> None:
        pass
    def handle(self,codex:str)->"TAGState":
        pass 
class XState(TAGState):
    def __init__(self,context:"Solution",stack=[]) -> None:
        self.stack=stack
        self.context=context
    def handle(self,codex: str) -> "TAGState":
        if not self.stack: 
            if codex=="<":
                self.stack.append("<")
                return self 
            else:
                self.stack.append(codex)
                return TextState(self.context,self.stack)# 进入文本识别状态
        if  self.stack and self.stack[-1]=="<":
            if codex=="/":
                return CloseTAGState(self.context,["<","/"]) # 进入关闭识别状态
            if codex=="!":
                return CDataState(self.context,["<","!"]) # 进入识别text状态
            if codex.isupper():
                return StartTAGNameState(self.context,["<",codex])# 识别到新的TAG状态.
            return ErrorSTate()# 错误的内容。
class CDataState(TAGState):
    def __init__(self, context: "Solution",stack=[]) -> None:
        self.context=context
        self.stack=stack
        self.checkBegin=True 
        self.expectLetter="<![CDATA["
        self.checkIndex=2
        self.checkEnd=False 
        self.expectEndLetter="]]>"
        
    def handle(self, codex: str) -> "TAGState":
        if self.checkBegin :
            if self.expectLetter[self.checkIndex]==codex:
                self.checkIndex+=1
                if self.checkIndex>=len(self.expectLetter):
                    self.checkBegin=False 
                return self 
            else:
                return ErrorSTate()
        if not self.checkEnd :
            if codex=="]":# 进入到识别结束字符位置。
                self.checkEnd=True 
                self.checkIndex=1
            return self 
        else:
            if codex==self.expectEndLetter[self.checkIndex]:
                self.checkIndex+=1
                if self.checkIndex>=len(self.expectEndLetter):
                    return XState(self.context,[])#识别完了CDATA_CONTENT
                return self
            else:
                # 恢复状态。
                self.checkIndex=0
                self.checkEnd=False 
                return self #继续CDATA_CONTENT识别。

class TextState(TAGState):
    def __init__(self, context: "Solution",stack=[]) -> None:
        self.stack=stack  
        self.context=context
    def handle(self, codex: str) -> "TAGState":
        if codex!="<":
            self.stack.append(codex)
            return self 
        return XState(self.context,["<"])
        

class ErrorSTate(TAGState):
    def __init__(self, context: "Solution"=None,stack=[]) -> None:
        self.stack=stack  
        self.context=context
class EndSTate(TAGState):
    def __init__(self, context: "Solution"=None,stack=[]) -> None:
        self.stack=stack  
        self.context=context
class CloseTAGState(TAGState):
    def __init__(self, context: "Solution",stack=[]) -> None:
        self.stack=stack  
        self.context=context
    def handle(self,codex: str) -> "TAGState":
        if codex!=">":
            if not codex.isupper():
                return ErrorSTate()
            self.stack.append(codex)
            if len(self.stack)>11:
                return ErrorSTate() 
            return self
        else:
            tagname=self.stack[2:]
            if  self.context and   self.context.stateStack[-1]==tagname:
                self.context.stateStack.pop() #消除close tag。
                return EndSTate(self.context,[])
            else:
                return  ErrorSTate() # 状态不匹配的情况
            


class StartTAGNameState(TAGState):
    def __init__(self,context:"Solution",stack:List=[]) -> None:
        self.stack=stack
        self.context=context
    def handle(self,codex:str)->"TAGState":
        if codex.isupper():
            self.stack.append(codex)
            if len(self.stack)>10:
                return ErrorSTate()
            return self 
        elif codex==">":
            if len(self.stack)==1:
                return ErrorSTate() # tag len in [1,9]
            self.context.stateStack.append(self.stack[1:])# 保留状态
            return  XState(self.context,[])
        return ErrorSTate()
class InitState(TAGState):
    def __init__(self, context: "Solution", stack=[]) -> None:
        self.stack=stack
        self.context=context
    def handle(self, codex: str) -> "TAGState":
        if codex!="<":
            return ErrorSTate()
        return StartTAGNameState(self.context,["<"])
class Solution:
    """
    Runtime: 73 ms, faster than 5.60% of Python3 online submissions for Tag Validator.
    Memory Usage: 14.2 MB, less than 16.80% of Python3 online submissions for Tag Validator.
    """
    def __init__(self) -> None:
        self.stateStack=[]
    def isValid(self, code: str) -> bool:
        currentState=InitState(self,[])
        for x in code:
            if isinstance(currentState,EndSTate) :
                if  self.stateStack:
                    currentState=XState(self,[])
                else:
                    return False
            currentState=currentState.handle(x)
            if isinstance(currentState,ErrorSTate):
                return False 
        if self.stateStack:
            return False
        if isinstance(currentState,EndSTate):
            return True
        return False 

def testCase0(instance:Solution=Solution()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")

    print(instance.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>")==True)
    print(instance.isValid( "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")==True)
    print(instance.isValid( "<A>  <B> </A>   </B>")==False)
    print(instance.isValid( "<AAAAAAAAAAAA>   </AAAAAAAAAAAA>")==False)
    print(instance.isValid( "<DIV>>>  ![cdata[]] <![CDATA<div>]>]]>]]>>]</DIV>")==False)
    print(instance.isValid( "<A>  </A><B>    </B>")==False)

def wrongCase(instance:Solution=Solution()):
    print(instance.isValid("<A><A>/A></A></A>"))
    print(instance.isValid("<A"))
if __name__ =="__main__":
    #testCase0()
    #testCase0()
    wrongCase()