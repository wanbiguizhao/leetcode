
from collections import Counter
def is_repeat_subseq_in(seq:list[int],sub_seq_k:int):
    """
    理解:
    1.要求连续的子序列，就可以认为是一个字符串匹配的问题。
    2. 滑动窗口长度为seb_seq_k作为key，query窗口右边的字符串，找到则返回true。
    3. 字符串匹配采用KMP算法进行，整体的时间复杂度O(n**2)。
    in：[1,1,2,3,4,2,3,4] 4 
    out： False
    -----
    in [1,2,3,4,22,1,2,3,4] 4 
    out True
    """
    def make_next(sub_seq):
        next_kmp=[0]*(sub_seq_k)
        k=0
        q=1
        while q<sub_seq_k:
            while k>0 and sub_seq[k]!=sub_seq[q]:
                k=next_kmp[k-1]
            if (sub_seq[q]==sub_seq[k]):
                k+=1
            next_kmp[q]=k
            q+=1
        return next_kmp

    def kmp(sub_seq,target_seq):
        next_kmp=make_next(sub_seq)
        sub_seq_index=0
        target_seq_index=0
        while target_seq_index<len(target_seq):#target_seq 还有足够的空间进行搜索。 
            while sub_seq_index>0 and sub_seq[sub_seq_index]!=target_seq[target_seq_index]:
                sub_seq_index=next_kmp[sub_seq_index-1]
            if sub_seq[sub_seq_index]==target_seq[target_seq_index]:
                sub_seq_index+=1
            if sub_seq_index==len(sub_seq):
                return True
            target_seq_index+=1
        return False
    Const_seq_len=len(seq)
    if sub_seq_k+1>Const_seq_len:
        #seq长度不满足两个连续的子序列。
        return False
    if sub_seq_k==1:
        # 特殊的例子，指定子序列长度为1时
        counter=Counter(seq)
        if max(counter.values())>1:
            return True
        return False 
    sub_seq_begin=0 #表示子序列 seq[sub_seq_begin,sub_seq_begin+sub_seq_k-1]表示连续子序列。
    while sub_seq_begin+1+sub_seq_k<=Const_seq_len:# 表示剩余搜索的空间够sub_seq_k的子序列
        if kmp( seq[sub_seq_begin: sub_seq_begin+sub_seq_k], seq[ sub_seq_begin+1:]):
            # 考虑到代码可读性（减少在seq使用相对index）可以接受开辟了O(n)的内存空间，
            return True
        sub_seq_begin+=1# 窗口移动。
    return False
# 根据题意的测试用例
assert is_repeat_subseq_in([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],6)==True
assert is_repeat_subseq_in([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],5)==True
assert is_repeat_subseq_in([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],4)==True
assert is_repeat_subseq_in([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],3)==True
assert is_repeat_subseq_in([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],7)==False
# 边界测试
assert is_repeat_subseq_in([1,2,2,3,4,5,1,2,3,4],6)==False
assert is_repeat_subseq_in([2,2,2,2,2,2,2,2,2,2],5)==True
assert is_repeat_subseq_in([1,2,3,2,3],1)==True
assert is_repeat_subseq_in([1,2,3,2,3],2)==True
assert is_repeat_subseq_in([2,2,3,3,2,2,1,3,4],3)==False
assert is_repeat_subseq_in([2,2,3,2,2,2,1,3,4],3)==False

assert is_repeat_subseq_in([2,2,2,2,2],4)==True
assert is_repeat_subseq_in([2,2,2,2,2],5)==False


# 性能测试
# 0.017 second
assert is_repeat_subseq_in(list(range(300))+[291,292,293],3)==True
# 0.5 second
assert is_repeat_subseq_in(list(range(3000))+[2901,2902,2903],3)==True
assert is_repeat_subseq_in(list(range(3000))+[2901,2902,2903],100)==False

# 53 second
# assert is_repeat_subseq_in(list(range(30000))+[29001,29002,29003],3)==True
