Stack and Queue 

```py
push(x) # 将一个元素放入队列的尾部。
pop() # 从队列首部移除元素。
peek() # 返回队列首部的元素。
empty() # 返回队列是否为空。
```



> [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
>
> 使用栈来模式队列的行为，如果仅仅用一个栈是不行的，所以需要两个栈**一个输入栈，一个输出栈**
>
> ![](https://code-thinking.cdn.bcebos.com/gifs/232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97%E7%89%88%E6%9C%AC2.gif)
>
> peek()的实现，直接复用了pop()， 要不然，对stOut判空的逻辑又要重写一遍。