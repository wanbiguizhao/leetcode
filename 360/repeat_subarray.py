
# %%
"""
第一种方法，立刻想到的dfs问题，从n中抽取m个数据，使用缓存，看一下有没有重复的字符串，时间复杂度特别高尤其是k略小于seq长度时。
设计测试用例时
输入：[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15],15 
发现对于15和15，对于长度k-1个子序列，只要后面存在2个以上相同的字符串时就意味有重复的字符串。
第二种方法：使用一个索引缓存，缓存某个数据的在seq中的索引，存错某个数字从右边向左出现的第二次的位置。
例如：[1,2,3,4,2,2] 对于2而言，存储位置4.
示例1:
[1,2,3,4,2,2] 要求子序列长度为5。从后向前扫描数组，先看到2，从缓存中找到2的前面索引位置为4，4+1(下标从0开始，补充1)>=5，返回True
示例2：
[1,2,3,2,4,2] 要求子序列长度为5。从后向前扫描数组，先看到2，从缓存中找到2的前面索引位置为3，3+1(下标从0开始，补充1)<5，不满足条件,继续扫描，知道扫描完所有的字符串。 
"""

"""
第一种方法实现：
"""
class RepeatSubarray:
    def is_repeat_subarray_in_seq(self,seq:list[int],seq_len_k:int):
        def dfs(ith,tmp_list):
            if self.bingo_flag:
                return 
            if len(tmp_list)==seq_len_k:
                sub_array="-".join(map(str,tmp_list))
                if sub_array in subarray_cache:
                    self.bingo_flag=True 
                else:
                    subarray_cache.add(sub_array)
                return
            if ith>=len(seq):
                return 
            dfs(ith+1,tmp_list+[seq[ith]])
            dfs(ith+1,tmp_list)
        if seq_len_k>=len(seq) :#or seq_len_k ==1:
            return False
        self.bingo_flag=False
        subarray_cache=set()# 缓存，用于标识字符串是否已经出现。
        dfs(0,[])
        return self.bingo_flag
checker=RepeatSubarray()
assert checker.is_repeat_subarray_in_seq([1,22,33,1,33],2)==True
assert checker.is_repeat_subarray_in_seq([1,2,3,4,5,1,2,3,4,5],5)==True
assert checker.is_repeat_subarray_in_seq([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],6)==True
# 边界检测
assert checker.is_repeat_subarray_in_seq([1,22,33,22,33],3)==True
assert checker.is_repeat_subarray_in_seq([1,1,22,33],3)==True
assert checker.is_repeat_subarray_in_seq([1,22,1,33,44],4)==False
assert checker.is_repeat_subarray_in_seq([1,22,22,1,1,22,33,44,55],5)==True
assert checker.is_repeat_subarray_in_seq([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15],15)==True
assert checker.is_repeat_subarray_in_seq(list(range(30)),3)==False
assert checker.is_repeat_subarray_in_seq([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],15)==True

# %%
"""
第二种测试：
"""
def is_repeat_subarray_in_seq(seq:list[int],sub_seq_k:int):
    if sub_seq_k>=len(seq):
        return False
    cache_index={}
    i=len(seq)-1
    while i>=0:
        if seq[i] not in cache_index:
            cache_index[seq[i]]=-1
        elif cache_index[seq[i]]==-1:
            cache_index[seq[i]]=i 
        i=i-1
    i=len(seq)-1
    while i>=0:
        if cache_index[seq[i]]!=-1 and cache_index[seq[i]]>=sub_seq_k-1:
            return True
        i-=1
    return False
#assert is_repeat_subarray_in_seq(list(range(300)),15)==False
"""
原题提供的测试用例
"""
assert is_repeat_subarray_in_seq([1,2,3,4,5,1,2,3,4,5],5)==True
assert is_repeat_subarray_in_seq([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],6)==True
assert is_repeat_subarray_in_seq([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],7)==True
assert is_repeat_subarray_in_seq([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],13)==True
assert is_repeat_subarray_in_seq([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],14)==True
assert is_repeat_subarray_in_seq([1,2,2,3,4,5,1,2,2,3,4,5,6,2,2,3],15)==True

"""
边界值测试
"""
assert is_repeat_subarray_in_seq([1,2,3,4,5,5],5)==True
assert is_repeat_subarray_in_seq([1,2,3,4,5,5,4,3,2,1],5)==True
assert is_repeat_subarray_in_seq([1,2,3,4,5,5,4,3,2,1],6)==False
assert is_repeat_subarray_in_seq([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15],15)==True

"""
根据题意，提前返回False
"""
assert is_repeat_subarray_in_seq([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15],17)==False
assert is_repeat_subarray_in_seq([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15],1)==True
assert is_repeat_subarray_in_seq([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],1)==False
"""
全路径测试
"""
assert is_repeat_subarray_in_seq(list(range(300))+list(range(300,0,-1)),2)==True
assert is_repeat_subarray_in_seq(list(range(300))+list(range(300)),400)==False
assert is_repeat_subarray_in_seq(list(range(300))+list(range(300)),300)==True
assert is_repeat_subarray_in_seq(list(range(300))+list(range(300)),1)==True
assert is_repeat_subarray_in_seq(list(range(300))+list(range(300))+list(range(300)),600)==True
assert is_repeat_subarray_in_seq(list(range(300))+list(range(300))+list(range(300)),601)==False

# %%
