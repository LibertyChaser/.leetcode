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
>  **括号==匹配是使用栈解决的经典问题==**
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



> [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) 
>
> 匹配问题
>
> ![](https://code-thinking.cdn.bcebos.com/gifs/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.gif)

```py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item: # 这里的if res非常巧妙 先看是不是空的 再比较
                res.pop()
            else:
                res.append(item)
        return "".join(res)  # 字符串拼接
```

```py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
          	# 这个题我没想到这种方法的原因是 我之前总是先判断再操作 但受限于可能所指的东西都是空的 而且条件其实也一直在变 也没法像27固定的判断那样直接移除元素
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])
```



>  [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
>
> ![](https://code-thinking.cdn.bcebos.com/gifs/150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.gif)

```python
from operator import add, sub, mul # 这个引用非常好

class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2)) # 第一个出来的在运算符后面
                # 这里直接用op_map来映射函数 省去了很多行代码
        return stack.pop()
```



>  [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
>
> 这个b题写的想死 毁灭吧 感觉讲的也不是很清楚 我的理解大概是这样的
>
> 

```py
from collections import deque

class MyQueue:  # 单调队列（从大到小
    def __init__(self):
        self.queue = deque()  # 这里需要使用deque实现单调队列，直接使用list会超时

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    # 同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()  # list.pop()时间复杂度为O(n),这里需要使用collections.deque()

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int): # -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k): #先将前k的元素放进队列
            que.push(nums[i])
        result.append(que.front()) #result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k]) #滑动窗口移除最前面元素
            que.push(nums[i]) #滑动窗口前加入最后面的元素
            result.append(que.front()) #记录对应的最大值
        return result
```





>  [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
>
> pri_que是小根堆
>
> heapq这玩意实际上是对于list 这里的list就是pri_que进行操作的 和我们之前理解的根堆还有所不同

```py
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #要统计元素出现频率
        map_ = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆
        
        #用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
        
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
```

```py
from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int): # -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
    
        pri_que = PriorityQueue()
        for key, freq in map_.items():
            pri_que.put((freq, key))
            if pri_que.qsize() > k:
                pri_que.get()

        return [pri_que.get()[1] for _ in range(k)]
```

