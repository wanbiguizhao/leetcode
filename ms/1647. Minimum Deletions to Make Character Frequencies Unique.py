from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        """_summary_

        Args:
            s (str): _description_

        Returns:
            int: _description_
        Runtime: 136 ms
        Memory Usage: 14.9 MB

        
        """
        # 采用递归思想，把大问题转换成小问题去进行解决。
        # 预处理问题。
        sCounter=Counter(s)# 记录每个字母对应频率
        # 第二次进行计数，记录每个频率对应个个数[[5,3],[4,2]] 表示有三个字母的频率为5，两个字母的频率为4
        freqCounter=Counter(sCounter.values())
        freqCountList=sorted([[k,v] for k,v in freqCounter.items()])
        deleteLetterCounter=0
        while freqCountList:
            numXfreq,counter =freqCountList.pop(-1)
            if numXfreq==0:
                break 
            if counter-1>0:
                deleteLetterCounter+=(counter-1)
                if freqCountList and freqCountList[-1][0]==numXfreq-1: # 合并
                    freqCountList[-1][1]+=counter-1
                else:
                    freqCountList.append([numXfreq-1,counter-1])
        return deleteLetterCounter

    def minDeletions(self, s: str) -> int:
        """_summary_

        Args:
            s (str): _description_

        Returns:
            int: _description_
        执行用时：
        104 ms
        , 在所有 Python3 提交中击败了
        93.57%
        的用户
        内存消耗：
        15.4 MB
        , 在所有 Python3 提交中击败了
        63.05%
        的用户
        通过测试用例：
        103 / 103
        
        """
        freqCounter=Counter(s)
        freqDescList=sorted(freqCounter.values(),reverse=True)
        freqUpperBoundary=freqDescList[0]
        ans=0
        for cnt in freqDescList:
            if freqUpperBoundary==0:
                ans+=cnt
            elif cnt<=freqUpperBoundary:
                freqUpperBoundary=cnt-1 
            else:
                ans+=cnt-freqUpperBoundary
                freqUpperBoundary-=1
        return ans  
        

def testCase_wrong(instance:Solution=Solution()):
    res=instance.minDeletions("aaabbbcc") # 错误原因freqCountList[-1][0] 搞错下标了
    print(res,res==2)
    
def testCase0(instance:Solution=Solution()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")
    res=instance.minDeletions("aaabbc")
    print(res,res==0)
    res=instance.minDeletions("aaaaabbbbbccccc")
    print(res,res==3)
    res=instance.minDeletions("aaabbbcccddd")
    print(res,res==6)
if __name__ =="__main__":
    #testCase0()
    testCase0()
    testCase_wrong()
        