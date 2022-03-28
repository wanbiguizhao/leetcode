
from msilib.schema import SelfReg
from platform import node
from turtle import left, right, update
import pysnooper
from typing import List
from copy import copy


class Solution:
    @pysnooper.snoop()
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        ans = []
        s = list(s)
        currentMaxLengthRepeating, range_left_index, range_right_index = self.getLengthOfLongestRepeatingCharacter(
            s)
        for index in range(len(queryCharacters)):
            s[queryIndices[index]] = queryCharacters[index]
            if queryIndices[index] >= range_left_index and queryIndices[index] < range_right_index:
                currentMaxLengthRepeating, range_left_index, range_right_index = self.getLengthOfLongestRepeatingCharacter(
                    s)
            else:
                max_char, o_range_left_index, o_range_right_index = self.searchRepeatingCharacter(
                    s, queryIndices[index])
                if max_char > currentMaxLengthRepeating:
                    currentMaxLengthRepeating, range_left_index, range_right_index = max_char, o_range_left_index, o_range_right_index
            ans.append(currentMaxLengthRepeating)
        return ans

    def searchRepeatingCharacter(self, s, index):
        left_index = index
        while left_index >= 0 and s[left_index] == s[index]:
            left_index -= 1

        right_index = index
        while right_index < len(s) and s[right_index] == s[index]:
            right_index += 1
        return right_index-left_index-1, max(left_index, 0), right_index

    def getLengthOfLongestRepeatingCharacter(self, s):
        if len(s) == 1:
            return 1, 0, 1
        max_length = 1
        beg_index = 0
        current_index = beg_index+1
        range_left_index = beg_index
        range_right_index = beg_index+1  # like  [)
        while current_index < len(s):
            if s[beg_index] == s[current_index]:
                current_index += 1
            else:
                if max_length < current_index-beg_index:
                    max_length = current_index-beg_index
                    range_left_index = beg_index
                    range_right_index = current_index
                max_length = max(max_length, current_index-beg_index)
                beg_index = current_index
                current_index = beg_index+1
        if current_index-beg_index > max_length:
            max_length = max(max_length, current_index-beg_index)
            range_left_index = beg_index
            range_right_index = current_index
        return max_length, range_left_index, range_right_index


class SegmentTree:
    def __init__(self, data) -> None:
        self.nodes = [None]*4*len(data)
        self.data = data
        self._build_tree(0, 0, len(data)-1)

    def _left(self, index):
        return (index+1)*2-1

    def _right(self, index):
        return (index+1)*2
    #@pysnooper.snoop()
    def _build_tree(self, node_index, left_data_index, right_data_index):
        # (longest c, longest len ,prefix c ,prefix len, suffix c , suffix len)
        value = None
        if left_data_index == right_data_index:
            value = (
                self.data[left_data_index],
                1,
                self.data[left_data_index],
                1,
                self.data[left_data_index],
                1
            )
        else:
            left_node_index = self._left(node_index)
            right_node_index = self._right(node_index)
            mid_data_index = (left_data_index+right_data_index)//2
            (left_lc, left_ll, left_pc, left_pl, left_sc, left_sl) = self._build_tree(
                left_node_index, left_data_index, mid_data_index)
            (right_lc, right_ll, right_pc, right_pl, right_sc, right_sl) = self._build_tree(
                right_node_index, mid_data_index+1, right_data_index)
            lc = ll = None 
            

            if left_ll > right_ll:
                ll = left_ll
                lc = left_lc
            else:
                ll = right_ll
                lc = right_lc
            if left_sc == right_pc and left_sl + right_pl > ll:
                ll = left_sl+right_pl
                lc = left_sc
            # construct prefix
            pc = left_pc
            pl = left_pl
            if pl == mid_data_index - left_data_index + 1 and pc == right_pc:
                pl = pl + right_pl
            sc = right_sc
            sl = right_sl
            if sl == right_data_index - mid_data_index and sc == left_sc:
                sl = sl + left_sl
            value = (lc, ll, pc, pl, sc, sl)
        self.nodes[node_index] = value
        return value

    def _update_tree(self, node_index, data_index, update_value, left_data_index, right_data_index):
        value=self.nodes[node_index]
        mid_data_index= ( left_data_index+right_data_index )//2 
        left_node_index= self._left(node_index)
        right_node_index= self._right(node_index)
        new_value=None 
        if left_data_index == right_data_index:
            new_value=(
                update_value,
                1,
                update_value,
                1,
                update_value,
                1
            )
        else :
            left_value = right_value = None 
            if data_index <= mid_data_index:
                left_value = self._update_tree(left_node_index,data_index,update_value,left_data_index,mid_data_index)
                right_value = self.nodes[right_node_index]
            else:
                left_value = self.nodes[left_node_index]
                right_value = self._update_tree(right_node_index,data_index,update_value,mid_data_index+1,right_data_index)
            (left_lc,left_ll,left_pc,left_pl,left_sc,left_sl)=left_value
            (right_lc,right_ll,right_pc,right_pl,right_sc,right_sl)=right_value
            ll=lc=None 
            if left_ll>right_ll:
                ll=left_ll
                lc=left_lc
            else:
                ll=right_ll
                lc=right_lc 
            if left_sc == right_pc and ll < left_sl+ right_pl:
                ll=left_sl+ right_pl
                #lc=left_sc 
            pl=left_pl
            if left_pl == mid_data_index+1-left_data_index and left_pc == right_pc:
                pl=left_pl+right_pl 
            sl= right_sl
            if right_sl == right_data_index - mid_data_index and right_sc == left_sc:
                sl= right_sl + left_sl
            new_value=(lc,ll,left_pc,pl,right_sc,sl)
        self.nodes[node_index]=new_value
        return new_value
    
    def update_tree(self,data_index,data_value):
        self._update_tree(0,data_index,data_value,0,len(self.data)-1)


class Solution:
    #@pysnooper.snoop()
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        ans = []
        segment_tree=SegmentTree(s)
        for index in range(len(queryCharacters)):
            segment_tree.update_tree(queryIndices[index],queryCharacters[index])
            ans.append( segment_tree.nodes[0][1])
            #ans.append(currentMaxLengthRepeating)
        return ans



            


if __name__ == "__main__":
    instance = Solution()
    # instance.longestRepeating("babaccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"*200,"bcb",[1,3,3])
    instance.longestRepeating(
        "wnkkqiajlwruouqntdvujfgdhcyanunitzcxtzlhkjvftsgcetlddjjppdcgfcauslpvbiypinpksrlhelxqxtyhsxinezmk",
"rfycdgwixoqpcjiivildoukpxhocimnnvztsixyaiayagbtxwdniojsodrahtspqbetwbgtttquqcawudvokbtqpxxgscniauf",
[62,60,61,85,61,58,72,95,11,52,77,27,41,1,93,70,26,80,56,44,46,3,92,65,19,5,6,73,26,38,59,28,42,28,24,51,91,35,84,94,78,17,92,40,87,48,94,18,6,8,35,20,30,46,35,34,77,25,33,25,87,74,94,36,9,39,30,88,90,92,64,13,10,29,4,60,46,49,29,79,3,22,12,36,67,90,67,71,63,45,57,52,52,67,77,89,37,49])
