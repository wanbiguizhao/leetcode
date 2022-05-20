from typing import List 
from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def get_neighbour_coor(x,y):
            directions=[
                [0,1],
                [1,0],
                [0,-1],
                [-1,0]
            ]
            for direct in directions:
                xd,yd=x+direct[0],y+direct[1]
                if xd>=0 and xd<const_m and yd>=0 and yd<const_n and (xd,yd) not in visited_set:# 这个要做一个某个字母是否已经用过了。
                    yield (xd,yd)
        # 还是使用递归吧。
        def findword(word:str,pre_coordinate_list):
            if not word:
                return True 
            if word[0] not in coordinate_cache:
                return False
            if not pre_coordinate_list:
                return False
            for coor_current in coordinate_cache[word[0]]:
                if coor_current in pre_coordinate_list:
                    #pass_coor.append(coor_current) # 这几个坐标是可以使用的。 
                    (x,y)=coor_current
                    visited_set.add((x,y)) # 不使用递归状态的保存和回退特别的难
                    next_coordinate_list=list(get_neighbour_coor(x,y))
                    if findword(word[1:],next_coordinate_list):
                        return True 
                    visited_set.remove(coor_current)
            return False 
        coordinate_cache=defaultdict(list)
        const_m,const_n=len(board),len(board[0])
        for m in range(const_m):
            for n in range(const_n):
                coordinate_cache[board[m][n]].append((m,n))
        ans_list=[]
        for index,word in enumerate(words):
            print(index,word,(index+1)/len(words))
            visited_set=set()
            if word[0] not in coordinate_cache:
                continue
            else:
                for (x,y) in coordinate_cache[word[0]]:
                    coor_queue=list(get_neighbour_coor(x,y))
                    visited_set.add((x,y))
                    if findword(word[1:],coor_queue):
                        ans_list.append(word)
                        break
                    visited_set.remove((x,y))
        return ans_list
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 尝试使用trie前缀树进行缓存。
        def getNeighbourCooridate(x,y):
            directions=[
                [0,1],
                [1,0],
                [0,-1],
                [-1,0]
            ]
            for direct in directions:
                xd,yd=x+direct[0],y+direct[1]
                if xd>=0 and xd<const_m and yd>=0 and yd<const_n  and visited[xd][yd]==0:# 这个要做一个某个字母是否已经用过了。
                    yield (xd,yd)
        def dfs(spaceDataDict:dict,prefix,conditionCoordinateList):
            """_summary_

            Args:
                spaceDataDict (_type_): 搜索空间，基于字典构造的树
                prefix (_type_): 已经搜索的前缀字符
                conditionCoordinateList (_type_): 约束条件，当前搜索的字母的坐标必须在conditionCoordinateList中。

            Returns:
                _type_: _description_
            """
            if spaceDataDict["$"]==True:
                ans_list.append(prefix)# 表示已经搜索到一个完整的单词了。
                tree_root.disable(prefix) # 在Tire中逻辑删除prefix的痕迹。
                spaceDataDict["$"]=False# 这个单词可以不再进行匹配了，但是还是会被搜索。
            #     spaceDataDict["word_count"]-=1
            # if spaceDataDict["word_count"]==0:
            #     return # 这个单词已经搜索过了并且没有前缀是该单词的前缀了。
            for xchar,subSpaceDataDict in spaceDataDict.items():
                if xchar=="$" or xchar=="word_count":
                    continue # 特殊情况
                for (x,y) in coordinate_cache[xchar]:# 当前字母xchar可能存在的坐标
                    if subSpaceDataDict["word_count"]==0:
                        # xchar 还对应的没有找到word的个数。
                        continue 
                    if visited[x][y]==1:
                        continue # 已经访问过了跳过
                    if (x,y) in conditionCoordinateList: # 是否符合conditionCoordinateList的约束条件
                        # 当然会有一些重复搜索的问题在里面，例如整个矩阵中，存在两个以上的方案，可以找到到eats，其中一个eats找到之后，没有办法阻止继续搜索eats的结果。
                        # 这个时候就要找到(x,y)的邻居点作为新的conditionCoordinateList
                        newConditionCoordinateList=list(getNeighbourCooridate(x,y))
                        visited[x][y]=1
                        dfs(subSpaceDataDict,prefix+xchar,newConditionCoordinateList)
                        visited[x][y]=0
        tree_root=Trie()
        for word in words:
            # 构建前缀树
            tree_root.insert(word)
        coordinate_cache=defaultdict(list)
        const_m,const_n=len(board),len(board[0])
        visited=[ ]# 比set效率高，记录哪些字典被访问了。
        for m in range(const_m):
            visited.append([])
            for n in range(const_n):
                coordinate_cache[board[m][n]].append((m,n))
                visited[m].append(0)
        ans_list=[]
        for xchar,subSpaceDataDict in tree_root.core_dict.items():
            if xchar=="$":
                continue 
            for (x,y) in coordinate_cache[xchar]:
                visited[x][y]=1
                conditionCoordinateList=list(getNeighbourCooridate(x,y))
                dfs(subSpaceDataDict,xchar,conditionCoordinateList)
                visited[x][y]=0
        print(ans_list)
        return ans_list
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 尝试使用trie前缀树进行缓存。
        # 使用集合运算，提升速度
        def getNeighbourCooridate(x,y):
            directions=[
                [0,1],
                [1,0],
                [0,-1],
                [-1,0]
            ]
            for direct in directions:
                xd,yd=x+direct[0],y+direct[1]
                if xd>=0 and xd<const_m and yd>=0 and yd<const_n  and visited[xd][yd]==0:# 这个要做一个某个字母是否已经用过了。
                    yield (xd,yd)
        def dfs(spaceDataDict:dict,prefix,conditionCoordinateList):
            """_summary_

            Args:
                spaceDataDict (_type_): 搜索空间，基于字典构造的树
                prefix (_type_): 已经搜索的前缀字符
                conditionCoordinateList (_type_): 约束条件，当前搜索的字母的坐标必须在conditionCoordinateList中。

            Returns:
                _type_: _description_
            """
            if spaceDataDict["$"]==True:
                ans_list.append(prefix)# 表示已经搜索到一个完整的单词了。
                tree_root.disable(prefix) # 在Tire中逻辑删除prefix的痕迹。
                spaceDataDict["$"]=False# 这个单词可以不再进行匹配了，但是还是会被搜索。
            #     spaceDataDict["word_count"]-=1
            # if spaceDataDict["word_count"]==0:
            #     return # 这个单词已经搜索过了并且没有前缀是该单词的前缀了。
            for xchar,subSpaceDataDict in spaceDataDict.items():
                if xchar=="$" or xchar=="word_count":
                    continue # 特殊情况
                for (x,y) in coordinate_cache[xchar] & conditionCoordinateList :# 求两个条件的交集
                    if subSpaceDataDict["word_count"]==0:
                        # xchar 还对应的没有找到word的个数。
                        continue 
                    if visited[x][y]==1:
                        continue # 已经访问过了跳过
                    # if (x,y) in conditionCoordinateList: # 是否符合conditionCoordinateList的约束条件
                    #     # 当然会有一些重复搜索的问题在里面，例如整个矩阵中，存在两个以上的方案，可以找到到eats，其中一个eats找到之后，没有办法阻止继续搜索eats的结果。
                    #     # 这个时候就要找到(x,y)的邻居点作为新的conditionCoordinateList
                    newConditionCoordinateList=set(getNeighbourCooridate(x,y))
                    visited[x][y]=1
                    dfs(subSpaceDataDict,prefix+xchar,newConditionCoordinateList)
                    visited[x][y]=0
        tree_root=Trie()
        for word in words:
            # 构建前缀树
            tree_root.insert(word)
        coordinate_cache=defaultdict(set)
        const_m,const_n=len(board),len(board[0])
        visited=[ ]# 比set效率高，记录哪些字典被访问了。
        for m in range(const_m):
            visited.append([])
            for n in range(const_n):
                coordinate_cache[board[m][n]].add((m,n))
                visited[m].append(0)
        ans_list=[]
        for xchar,subSpaceDataDict in tree_root.core_dict.items():
            if xchar=="$":
                continue 
            for (x,y) in coordinate_cache[xchar]:
                visited[x][y]=1
                conditionCoordinateList=set(getNeighbourCooridate(x,y))
                dfs(subSpaceDataDict,xchar,conditionCoordinateList)
                visited[x][y]=0
        print(ans_list)
        return ans_list
              


class Trie:
    # 考察面向对象和数据结构

    def __init__(self):
        self.core_dict={"$":False,"word_count":0}# word_count 表示某个字母被N个单词使用
        # 通过"$" 区分前缀还是单词
        # 使用字典作为树的存储。
        

    def insert(self, word: str) -> None:
        x_dict=self.core_dict
        for w in  word:
            if w in x_dict:
                x_dict=x_dict[w]
                x_dict["word_count"]+=1
            else:
                x_dict[w]={"$":False,"word_count":1}
                x_dict= x_dict[w]
        x_dict["$"]=True
    def disable(self,word)->None:
        """_summary_

        Args:
            word (_type_): 逻辑删除word的在树中的痕迹。
        """        
        x_dict=self.core_dict
        for w in  word:
            x_dict=x_dict[w]
            x_dict["word_count"]-=1
if __name__ == "__main__":
    instance=Solution()
    instance.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain","aaa"])
    instance.findWords([["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"]],["ababababaa","ababababab","ababababac","ababababad","ababababae","ababababaf","ababababag","ababababah","ababababai","ababababaj","ababababak","ababababal","ababababam","ababababan","ababababao","ababababap","ababababaq","ababababar","ababababas","ababababat","ababababau","ababababav","ababababaw","ababababax","ababababay","ababababaz","ababababba","ababababbb","ababababbc","ababababbd","ababababbe","ababababbf","ababababbg","ababababbh","ababababbi","ababababbj","ababababbk","ababababbl","ababababbm","ababababbn","ababababbo","ababababbp","ababababbq","ababababbr","ababababbs","ababababbt","ababababbu","ababababbv","ababababbw","ababababbx","ababababby","ababababbz","ababababca","ababababcb","ababababcc","ababababcd","ababababce","ababababcf","ababababcg","ababababch","ababababci","ababababcj","ababababck","ababababcl","ababababcm","ababababcn","ababababco","ababababcp","ababababcq","ababababcr","ababababcs","ababababct","ababababcu","ababababcv","ababababcw","ababababcx","ababababcy","ababababcz","ababababda","ababababdb","ababababdc","ababababdd","ababababde","ababababdf","ababababdg","ababababdh","ababababdi","ababababdj","ababababdk","ababababdl","ababababdm","ababababdn","ababababdo","ababababdp","ababababdq","ababababdr","ababababds","ababababdt","ababababdu","ababababdv","ababababdw","ababababdx","ababababdy","ababababdz","ababababea","ababababeb","ababababec","ababababed","ababababee","ababababef","ababababeg","ababababeh","ababababei","ababababej","ababababek","ababababel","ababababem","ababababen","ababababeo","ababababep","ababababeq","ababababer","ababababes","ababababet","ababababeu","ababababev","ababababew","ababababex","ababababey","ababababez","ababababfa","ababababfb","ababababfc","ababababfd","ababababfe","ababababff","ababababfg","ababababfh","ababababfi","ababababfj","ababababfk","ababababfl","ababababfm","ababababfn","ababababfo","ababababfp","ababababfq","ababababfr","ababababfs","ababababft","ababababfu","ababababfv","ababababfw","ababababfx","ababababfy","ababababfz","ababababga","ababababgb","ababababgc","ababababgd","ababababge","ababababgf","ababababgg","ababababgh","ababababgi","ababababgj","ababababgk","ababababgl","ababababgm","ababababgn","ababababgo","ababababgp","ababababgq","ababababgr","ababababgs","ababababgt","ababababgu","ababababgv","ababababgw","ababababgx","ababababgy","ababababgz","ababababha","ababababhb","ababababhc","ababababhd","ababababhe","ababababhf","ababababhg","ababababhh","ababababhi","ababababhj","ababababhk","ababababhl","ababababhm","ababababhn","ababababho","ababababhp","ababababhq","ababababhr","ababababhs","ababababht","ababababhu","ababababhv","ababababhw","ababababhx","ababababhy","ababababhz","ababababia","ababababib","ababababic","ababababid","ababababie","ababababif","ababababig","ababababih","ababababii","ababababij","ababababik","ababababil","ababababim","ababababin","ababababio","ababababip","ababababiq","ababababir","ababababis","ababababit","ababababiu","ababababiv","ababababiw","ababababix","ababababiy","ababababiz","ababababja","ababababjb","ababababjc","ababababjd","ababababje","ababababjf","ababababjg","ababababjh","ababababji","ababababjj","ababababjk","ababababjl","ababababjm","ababababjn","ababababjo","ababababjp","ababababjq","ababababjr","ababababjs","ababababjt","ababababju","ababababjv","ababababjw","ababababjx","ababababjy","ababababjz","ababababka","ababababkb","ababababkc","ababababkd","ababababke","ababababkf","ababababkg","ababababkh","ababababki","ababababkj","ababababkk","ababababkl","ababababkm","ababababkn","ababababko","ababababkp","ababababkq","ababababkr","ababababks","ababababkt","ababababku","ababababkv","ababababkw","ababababkx","ababababky","ababababkz","ababababla","abababablb","abababablc","ababababld","abababable","abababablf","abababablg","abababablh","ababababli","abababablj","abababablk","ababababll","abababablm","ababababln","abababablo","abababablp","abababablq","abababablr","ababababls","abababablt","abababablu","abababablv","abababablw","abababablx","abababably","abababablz","ababababma","ababababmb","ababababmc","ababababmd","ababababme","ababababmf","ababababmg","ababababmh","ababababmi","ababababmj","ababababmk","ababababml","ababababmm","ababababmn","ababababmo","ababababmp","ababababmq","ababababmr","ababababms","ababababmt","ababababmu","ababababmv","ababababmw","ababababmx","ababababmy","ababababmz","ababababna","ababababnb","ababababnc","ababababnd","ababababne","ababababnf","ababababng","ababababnh","ababababni","ababababnj","ababababnk","ababababnl","ababababnm","ababababnn","ababababno","ababababnp","ababababnq","ababababnr","ababababns","ababababnt","ababababnu","ababababnv","ababababnw","ababababnx","ababababny","ababababnz","ababababoa","ababababob","ababababoc","ababababod","ababababoe","ababababof","ababababog","ababababoh","ababababoi","ababababoj","ababababok","ababababol","ababababom","ababababon","ababababoo","ababababop","ababababoq","ababababor","ababababos","ababababot","ababababou","ababababov","ababababow","ababababox","ababababoy","ababababoz","ababababpa","ababababpb","ababababpc","ababababpd","ababababpe","ababababpf","ababababpg","ababababph","ababababpi","ababababpj","ababababpk","ababababpl","ababababpm","ababababpn","ababababpo","ababababpp","ababababpq","ababababpr","ababababps","ababababpt","ababababpu","ababababpv","ababababpw","ababababpx","ababababpy","ababababpz","ababababqa","ababababqb","ababababqc","ababababqd","ababababqe","ababababqf","ababababqg","ababababqh","ababababqi","ababababqj","ababababqk","ababababql","ababababqm","ababababqn","ababababqo","ababababqp","ababababqq","ababababqr","ababababqs","ababababqt","ababababqu","ababababqv","ababababqw","ababababqx","ababababqy","ababababqz","ababababra","ababababrb","ababababrc","ababababrd","ababababre","ababababrf","ababababrg","ababababrh","ababababri","ababababrj","ababababrk","ababababrl","ababababrm","ababababrn","ababababro","ababababrp","ababababrq","ababababrr","ababababrs","ababababrt","ababababru","ababababrv","ababababrw","ababababrx","ababababry","ababababrz","ababababsa","ababababsb","ababababsc","ababababsd","ababababse","ababababsf","ababababsg","ababababsh","ababababsi","ababababsj","ababababsk","ababababsl","ababababsm","ababababsn","ababababso","ababababsp","ababababsq","ababababsr","ababababss","ababababst","ababababsu","ababababsv","ababababsw","ababababsx","ababababsy","ababababsz","ababababta","ababababtb","ababababtc","ababababtd","ababababte","ababababtf","ababababtg","ababababth","ababababti","ababababtj","ababababtk","ababababtl","ababababtm","ababababtn","ababababto","ababababtp","ababababtq","ababababtr","ababababts","ababababtt","ababababtu","ababababtv","ababababtw","ababababtx","ababababty","ababababtz","ababababua","ababababub","ababababuc","ababababud","ababababue","ababababuf","ababababug","ababababuh","ababababui","ababababuj","ababababuk","ababababul","ababababum","ababababun","ababababuo","ababababup","ababababuq","ababababur","ababababus","ababababut","ababababuu","ababababuv","ababababuw","ababababux","ababababuy","ababababuz","ababababva","ababababvb","ababababvc","ababababvd","ababababve","ababababvf","ababababvg","ababababvh","ababababvi","ababababvj","ababababvk","ababababvl","ababababvm","ababababvn","ababababvo","ababababvp","ababababvq","ababababvr","ababababvs","ababababvt","ababababvu","ababababvv","ababababvw","ababababvx","ababababvy","ababababvz","ababababwa","ababababwb","ababababwc","ababababwd","ababababwe","ababababwf","ababababwg","ababababwh","ababababwi","ababababwj","ababababwk","ababababwl","ababababwm","ababababwn","ababababwo","ababababwp","ababababwq","ababababwr","ababababws","ababababwt","ababababwu","ababababwv","ababababww","ababababwx","ababababwy","ababababwz","ababababxa","ababababxb","ababababxc","ababababxd","ababababxe","ababababxf","ababababxg","ababababxh","ababababxi","ababababxj","ababababxk","ababababxl","ababababxm","ababababxn","ababababxo","ababababxp","ababababxq","ababababxr","ababababxs","ababababxt","ababababxu","ababababxv","ababababxw","ababababxx","ababababxy","ababababxz","ababababya","ababababyb","ababababyc","ababababyd","ababababye","ababababyf","ababababyg","ababababyh","ababababyi","ababababyj","ababababyk","ababababyl","ababababym","ababababyn","ababababyo","ababababyp","ababababyq","ababababyr","ababababys","ababababyt","ababababyu","ababababyv","ababababyw","ababababyx","ababababyy","ababababyz","ababababza","ababababzb","ababababzc","ababababzd","ababababze","ababababzf","ababababzg","ababababzh","ababababzi","ababababzj","ababababzk","ababababzl","ababababzm","ababababzn","ababababzo","ababababzp","ababababzq","ababababzr","ababababzs","ababababzt","ababababzu","ababababzv","ababababzw","ababababzx","ababababzy","ababababzz"])
    instance.findWords(board = [["a"]], words = ["a"])
    instance.findWords(board = [["a","a"]], words = ["aa"])
    instance.findWords(board =[["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]],words=["aaaaaaa"])#,"aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
