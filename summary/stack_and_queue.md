Stack and Queue 

**Queue**

```py
push(x) # 将一个元素放入队列的尾部。
pop() # 从队列首部移除元素。
peek() # 返回队列首部的元素。
empty() # 返回队列是否为空。
```

**Stack**

```py
push(x) # 元素 x 入栈
pop() # 移除栈顶元素
top() # 获取栈顶元素
empty() # 返回栈是否为空
```

一般来说我们用的最多的数据类型就是list

```python
>>> l = [1]
>>> l.append(2) # append 是加在最后面的
>>> l
[1, 2]
>>> l.pop() # pop 是让最后面的出来
2
```

注意有时候需要判断一下最后一个元素是不是空的：

```py
if res and res[-1] == item:
    res.pop()
```



以下两个题目的核心就是`pop()` 怎么写的问题

> [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
>
> 使用栈来模式队列的行为，如果仅仅用一个栈是不行的，所以需要两个栈**一个输入栈，一个输出栈**
>
> ![](https://code-thinking.cdn.bcebos.com/gifs/232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97%E7%89%88%E6%9C%AC2.gif)
>
> peek()的实现，直接复用了pop()， 要不然，对stOut判空的逻辑又要重写一遍。

```py
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int): # -> None:
        self.stack_in.append(x)

    def empty(self): # -> bool:
        return not (self.stack_in or self.stack_out)
      
    def pop(self): # -> int:
        if self.empty():
            return None
        if not self.stack_out:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self): # -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans


```



> [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
>
> **队列模拟栈，其实一个队列就够了**, 

```py
class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int): # -> None:
        self.que.append(x)

    def pop(self): # -> int:
        if self.empty():
            return None
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self): # -> int:
        ans = self.pop()
        self.que.append(ans)
        return ans

    def empty(self): # -> bool:
        return not self.que
```



> [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
>
>  **括号匹配是使用栈解决的经典问题**
>
> 出现左括号 就要把右括号放到栈里
>
> ==中间判断的时候一定要先看看是不是空的 再回溯==
>
> ![](https://code-thinking.cdn.bcebos.com/gifs/20.%E6%9C%89%E6%95%88%E6%8B%AC%E5%8F%B7.gif)

```py
class Solution:
    def isValid(self, s: str): # -> bool:
        stack = []
        for item in s:
            if item == "(":
                stack.append(")")
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")
            elif not stack or stack[-1] != item: # 顺序不能改变!!!
                return False
            else:
                stack.pop()
        return True if not stack else False
```



>  
>
> ![](https://code-thinking.cdn.bcebos.com/gifs/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.gif)
>
> 
