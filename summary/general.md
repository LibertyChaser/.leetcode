一般来说我们用的最多的数据类型就是list

```python
>>> l = [1]
>>> l.append(2) # append 是加在最后面的
>>> l
[1, 2]
>>> l.pop() # pop 是让最后面的出来
2
```

deque

```py
from collections import deque
que.append(x)
que.popleft()
que[0]
queue[-1]
```

注意有时候需要判断一下最后一个元素是不是空的：

```py
if res and res[-1] == item:
    res.pop()
```

dictionary

```py
map_ = {}
for i in range(len(nums)):
    map_[nums[i]] = map_.get(nums[i], 0) + 1 # 方括号
for key, freq in map_.items():
 		...
```

heapq

```py
import heapq 
...
        pri_que = [] #小顶堆
        
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出
                heapq.heappop(pri_que)

```

PriorityQueue

```py
from queue import PriorityQueue
...
        pri_que = PriorityQueue()
        for key, freq in map_.items():
            pri_que.put((freq, key)) # 这里是元组！！
            if pri_que.qsize() > k: # .qsize() not len()
                pri_que.get()

        return [pri_que.get()[1] for _ in range(k)]
```

