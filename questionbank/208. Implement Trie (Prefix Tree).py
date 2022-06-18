class Trie:
    # 考察面向对象和数据结构

    def __init__(self):
        self.core_dict={"$":False}
        # 通过"$" 区分前缀还是单词
        # 使用字典作为树的存储。
        

    def insert(self, word: str) -> None:
        x_dict=self.core_dict
        for w in  word:
            if w in x_dict:
                x_dict=x_dict[w]
            else:
                x_dict[w]={"$":False}
                x_dict= x_dict[w]
        x_dict["$"]=True 
        

    def search(self, word: str) -> bool:
        x_dict=self.core_dict
        for w in word:
            if w in x_dict:
                x_dict=x_dict[w]
            else:
                return False 
        return x_dict["$"] 
        

    def startsWith(self, prefix: str) -> bool:
        x_dict=self.core_dict
        for w in prefix:
            if w in x_dict:
                x_dict=x_dict[w]
            else:
                return False 
        return True 