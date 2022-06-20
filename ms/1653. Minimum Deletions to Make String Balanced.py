from os import rename


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        1653. Minimum Deletions to Make String Balanced
        对偶问题转换：对于第i个元素，前面有x个a和后面有y个b，那么对于i包含第i个元祖组成的balanced string的长度就是x+y+1 
        转换为，求x+y+1最长的的str。
        DP 的解法
        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        A_INDEX=0
        B_INDEX=1
        constSLEN=len(s)
        cache=[]
        for i in range(constSLEN):
            cache.append([0,0])
        # 初始化数据
        for i in range(constSLEN-1):
            cache[i+1][A_INDEX]=cache[i][A_INDEX]
            if s[i]=="a":
                cache[i+1][A_INDEX]=cache[i+1][A_INDEX]+1
        for i in range(constSLEN-2,-1,-1):
            cache[i][B_INDEX]=cache[i+1][B_INDEX]
            if s[i+1]=="b":
                cache[i][B_INDEX]=cache[i][B_INDEX]+1
            
        return constSLEN - max([count[A_INDEX]+count[B_INDEX]+1 for count in cache])
def testCase0(instance:Solution=Solution()):
    res=instance.minimumDeletions("aaabbaaa")
    print(res==2)
    res=instance.minimumDeletions("bbbbaaa")
    print(res==3)
if __name__ =="__main__":
    #testCase0()
    #testCase0()
    testCase0()