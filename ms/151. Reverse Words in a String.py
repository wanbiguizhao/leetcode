class Solution:
    def reverseWords(self, s: str) -> str:
        """
        151. Reverse Words in a String

        分治法的思想
        把 "     aaa      bbbb cccc    "
        拆成
        "     aaa"
        "      bbbb"
        " cccc"
        "   "
        Args:
            s (str): _description_

        Returns:
            str: _description_
        Runtime: 39 ms, faster than 78.43% of Python3 online submissions for Reverse Words in a String.
        Memory Usage: 14 MB, less than 47.55% of Python3 online submissions for Reverse Words in a String.
        """        
        constSLength=len(s)
        i=j=0 
        index=0
        ans_list=[]
        while index<constSLength:
            # 变成子问题去处理 变成[i,index)的进行处理
            while index<constSLength and  s[i]==" " and s[index]==" ":
                # 去除多余的空格
                index+=1
                i=index
            while index<constSLength and s[index]!=" ":
                # 填入单词
                index+=1
            if i<constSLength: # 边界值检测。
                ans_list.append(s[i:index]) 
            i=index# i指向第一个空格。
        return " ".join(ans_list[::-1])


def testCase0(instance:Solution=Solution()):
    # res=instance.reverseWords("    ")
    # print(res,res=="")
    # res=instance.reverseWords("    aaa   bb c")
    # print(res,res=="c bb aaa")
    res=instance.reverseWords("aaa   bb c   ")
    print(res,res=="c bb aaa")
if __name__ =="__main__":
    #testCase0()
    testCase0()