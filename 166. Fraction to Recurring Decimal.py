class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 核心问题在于发现循环的小数
        # 检查是否是负数的情况
        # 符号问题是一个大问题
        a= numerator
        b= denominator
        if a==0:
            return "0"
        if a%b==0:
            return str(a//b)
        str_ans=""
        if (a<0 and b>0) or (a>0 and b<0):
            str_ans="-"
        a=abs(a)
        b=abs(b)
        # 计算小数点前部分
        if a>b:
            str_ans+=str(a//b)
            str_ans+="."
            a=a%b
            a=a*10
        else :#a<b:
            a=a*10
            str_ans+="0."
        
        index_mapping={} #(商和余数)，重复出现代表有循环。
        #计算小数点后面的值
        while a!=0:
            if a<b:
                divide_num=0
            else:
                divide_num=a//b
                a=a%b
            help_key=(divide_num,a)
            if help_key in index_mapping:
                origin_index= index_mapping[help_key]
                # print(str_ans[:origin_index]+"("+str_ans[origin_index:len(str_ans)]+")")
                return str_ans[:origin_index]+"("+str_ans[origin_index:len(str_ans)]+")"
            str_ans+=str(divide_num)
            index_mapping[help_key]=len(str_ans)-1
            a=a*10            
            # 问题点在于如何检查是一个循环小数呢？
            # If multiple answers are possible, return any of them. 指的是循环小数。
        # print(str_ans)
        return str_ans


if __name__ == "__main__":
    instance=Solution()
    instance.fractionToDecimal(4,333)
    instance.fractionToDecimal(3334,333)
    instance.fractionToDecimal(1,6)
    instance.fractionToDecimal(6,1)
    instance.fractionToDecimal(10,3)
    instance.fractionToDecimal(0,3)
    instance.fractionToDecimal(-10,3)
