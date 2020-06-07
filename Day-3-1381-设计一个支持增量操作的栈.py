class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = [0] * maxSize             #初始化栈
        self.top = -1                               #当前栈顶


    def push(self, x: int) -> None:
        if self.top != len(self.stk) - 1:                  #判断当前元素的个数是否达到上限
            self.top += 1                                      #没有达到，就把 top 后移一个位置并添加一个元素
            self.stk[self.top] = x

    def pop(self) -> int:
        if self.top == -1:                                     #判断当前栈是否为空
            return -1                                            #为空返回-1
        self.top -= 1                                           #不空，将top前移一位
        return self.stk[self.top + 1]


    def increment(self, k: int, val: int) -> None:          #直接对栈底的最多k个元素加上val
        lim = min(k, self.top + 1)
        for i in range(lim):
            self.stk[i] += val