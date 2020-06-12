class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        #两个栈倒，新来的元素总是在栈底（队尾进）
        if self.stack1 == None: #stack1 is empty
            self.stack1.append(x)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop(-1))


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #直接弹出，本来就是队头出
        return self.stack1.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack1:
            return self.stack1[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # 因为队列１存储了所有元素，所以只需要判断队列１
        return len(self.stack1) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()