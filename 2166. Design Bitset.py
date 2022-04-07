

class Bitset:

    def __init__(self, size: int):
        self.size=size
        self.zero_size=size
        self.data="0"*self.size
        self.flip_data="1"*self.size
        

    def fix(self, idx: int) -> None:
        if self.data[idx]=="0":
            self.data = self.data[:idx] +"1"+self.data[idx+1:]
            self.flip_data = self.flip_data[:idx] + "0" + self.flip_data[idx+1:] 
            self.zero_size-=1


    def unfix(self, idx: int) -> None:
        if self.data[idx]=="1":
            self.data = self.data[:idx] +"0"+self.data[idx+1:]
            self.flip_data = self.flip_data[:idx] + "1" + self.flip_data[idx+1:]
            self.zero_size+=1
        

    def flip(self) -> None:
        self.data,self.flip_data = self.flip_data , self.data
        self.zero_size=self.size-self.zero_size

    def all(self) -> bool:
        return self.zero_size==0
        

    def one(self) -> bool:
        return self.zero_size!= self.size
        

    def count(self) -> int:
        return self.size -  self.zero_size
        

    def toString(self) -> str:
        return self.data
        