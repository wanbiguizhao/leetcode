class LinkNone:
    val:int 
    next=None
    pre=None

    def __init__(self,x:int):
        self.val=x 
        self.next=None
        self.pre=None

class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head_node=LinkNone(0)
        self.end_node=LinkNone(0)
        self.head_node.next=self.end_node
        self.end_node.pre=self.head_node

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        x_node=LinkNone(x)
        x_node.next=self.end_node
        x_node.pre=self.end_node.pre 
        self.end_node.pre.next=x_node
        self.end_node.pre=x_node
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        x_node=self.head_node.next 
        self.head_node.next=x_node.next
        x_node.next.pre= self.head_node

        return x_node.val

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.head_node.next.val

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.head_node.next == self.end_node

if __name__ == "__main__":
    queue=MyQueue()
    assert  queue.empty()==True 
    queue.push(1)
    queue.push(2)
    assert queue.peek()==1
    assert queue.pop()==1
    assert queue.empty()==False