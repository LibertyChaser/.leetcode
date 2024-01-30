array

python list常用方法

```python
>>> b = [1, 4, 0, 9]
>>> len(b)
4
>>> [0] * 5
[0, 0, 0, 0, 0]
>>> [[]] * 5
[[], [], [], [], []]
>>> b.append([])
>>> b
[0, 1, 4, 9, []]
```



| Method                                                       | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [append()](https://www.w3schools.com/python/ref_list_append.asp) | Adds an element at the end of the list                       |
| [copy()](https://www.w3schools.com/python/ref_list_copy.asp) | Returns a copy of the list                                   |
| [count()](https://www.w3schools.com/python/ref_list_count.asp) | Returns the number of elements with the specified value      |
| [extend()](https://www.w3schools.com/python/ref_list_extend.asp) | Add the elements of a list (or any iterable), to the end of the current list |
| [index()](https://www.w3schools.com/python/ref_list_index.asp) | Returns the index of the first element with the specified value |
| [insert()](https://www.w3schools.com/python/ref_list_insert.asp) | Adds an element at the specified position                    |
| [pop()](https://www.w3schools.com/python/ref_list_pop.asp)   | Removes the element at the specified position                |
| [remove()](https://www.w3schools.com/python/ref_list_remove.asp) | Removes the first item with the specified value              |
| [reverse()](https://www.w3schools.com/python/ref_list_reverse.asp) | Reverses the order of the list                               |
| [sort()](https://www.w3schools.com/python/ref_list_sort.asp) | Sorts the list                                               |

# Binary Search

> [704. Binary Search](https://leetcode.com/problems/binary-search/)
>
> Given an array of integers `nums` which ==is sorted== in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
>
> You must write an algorithm with `O(log n)` runtime complexity.
>
> **Constraints:**
>
> - `1 <= nums.length <= 104`
> - `-104 < nums[i], target < 104`
> - All the integers in `nums` are **==unique==**.
> - `nums` is sorted in ascending order.

1. **[left, right]**

```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # Here
        while (left <= right): # Here
            middle = left + (right - left) // 2
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                right = middle - 1 # 右边界也要被考虑
            elif (nums[middle] < target):
                left = middle + 1
        return -1
```

2. **[left, right)**

```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
  			left = 0
        right = len(nums) # Here
        while (left < right): # Here
            middle = (left + right) // 2
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                right = middle # 右边界不被考虑 所以无所谓
            elif (nums[middle] < target):
                left = middle + 1
        return -1
```

> [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
>
> 开头可以考虑增加一些特解 比如是最小的 或者 最大的

```py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)

        left, right = 0, len(nums)

        while (left < right):
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
              # 遇到答案也放到右边界 最后在循环结束时 left+1得 到的就是right 就是target的位置
              # 没答案的时候 left = right就是应该被插入的位置
                right = middle
        return left # 这里right也可以
```

> [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
>
> 对于上个题思想的综合运用

```py
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums, target):
            left, right = 0, len(nums)
            while (left < right):
                middle = left + (right - left) // 2
                if (nums[middle] < target):
                    left = middle + 1
                else:
                    right = middle
            return left # 这里right也可以

        left = search(nums, target)
        right = search(nums, target + 1) - 1

        if left <= right:
            return [left, right]

        return [-1, -1]
```

> [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
>
> 依旧是上个题综合应用 但这次找的是准确位置/应插入位置-1 
>
> 还一个不同是if条件变了

```py
class Solution:
    def mySqrt(self, x: int):# -> int:
        if x == 1:
            return 1
        left = 1
        right = x // 2 + 1
        while (left < right):
            middle = left + (right - left) // 2
            if middle ** 2 == x:
                return middle
            if middle ** 2 < x:
                left = middle + 1
            else:
                right = middle
        return left - 1
```

> [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
>
> 只是改变了条件而已

# Two Pointers

## 快慢指针法

**通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。** 

- 快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
- 慢指针：指向更新 新数组下标的位置

删除过程如下：

![](https://code-thinking.cdn.bcebos.com/gifs/27.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0-%E5%8F%8C%E6%8C%87%E9%92%88%E6%B3%95.gif)

> [27. Remove Element](https://leetcode.com/problems/remove-element/)
>
> 非常经典的双指针题目

```py
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:
            # 如果 fast 对应值不等于 val
            if nums[fast] != val: # 最好用 不等号 来作为分界 
              # 则把它与 slow 替换, slow 用来收集不等于 val 的值
                nums[slow] = nums[fast]
                slow += 1
            fast += 1 # 因为不管怎么样 fast始终在往前走
        return slow
```

或者改进一下用for

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
```

> [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
>
> 没什么新意 最后加个按顺序for填充即可

> [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)
>
> 这里就要用到list来记录了 也没什么新意的题目

> [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
>
> 做了一个小变体 就是fast什么时候往前走

```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        size = len(nums)
        while (fast < size):
            temp = nums[slow]
            if (nums[fast] == temp):
                fast += 1
            else: 
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
```

## 前后指针

> [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
>
> 这个题相当于是双指针从==一前一后==出发
>
> 注意顺序 如果是升序 从小到大 rslt = [new] + rslt

## Sliding window

所谓滑动窗口，**就是不断的调节子序列的起始位置和终止位置，从而得出我们要想的结果**。

外循环 表示 滑动窗口的终止位置 右边的

内循环 表示 滑动窗口的起始位置 左边的

这里还是以题目中的示例来举例，s=7， 数组是 2，3，1，2，4，3，来看一下查找的过程：

![](https://code-thinking.cdn.bcebos.com/gifs/209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.gif)

最后找到 4，3 是最短距离。

其实从动画中可以发现滑动窗口也可以理解为双指针法的一种！只不过这种解法更像是一个窗口的移动，所以叫做滑动窗口更适合一些。==窗口是左闭右闭的区间==

在本题中实现滑动窗口，主要确定如下三点：

- 窗口内是什么？
  - 窗口就是 满足其和 ≥ s 的长度最小的 连续 子数组。
- 如何移动窗口的起始位置？
  - 如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）
- 如何移动窗口的结束位置？
  - 窗口的结束位置就是遍历数组的指针，也就是for循环里的索引

> [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
>
> 非常经典的题目

```py
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]): # -> int:
        slow = 0
        size = len(nums)
        result = size + 1
        curr_sum = 0
        for i in range(size):
            curr_sum += nums[i]
            while (curr_sum >= target):
                result = min(result, i - slow + 1)
                curr_sum -= nums[slow]
                slow += 1
                    
        return result if result != size + 1 else 0
```

> [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
>
> 本质还是滑动窗口 也是左闭右闭的区间

```py
class Solution:
    def totalFruit(self, fruits: List[int]): # -> int:
        slow = 0
        result = 0
        record = {}
        size = len(fruits)
        for i in range(size):
            record[fruits[i]] = record.get(fruits[i], 0) + 1
            while (len(record) > 2):
                record[fruits[slow]] = record.get(fruits[slow], 0) - 1
                if record[fruits[slow]] == 0:
                    del record[fruits[slow]]
                slow += 1

            result = max(result, i - slow + 1)
        return result
```

# Spiral Matrix

这个就画图就可以了 一定清楚左闭右开的区间

> [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)
>
> 有点儿像是削洋葱 一层又一层的

```py
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        offset = 0
        filling = 1
        result = []
        mid = n // 2
        for i in range(n):
            result.append([0] * n)
        
        while (offset <= mid):
            
            for i in range(offset, n - offset - 1):
                result[offset][i] = filling
                filling += 1
            for i in range(offset, n - offset - 1):
                result[i][n - offset - 1] = filling
                filling += 1
            for i in range(n - offset - 1, offset, -1):
                result[n - offset - 1][i] = filling
                filling += 1
            for i in range(n - offset - 1, offset, -1):
                result[i][offset] = filling
                filling += 1
            offset += 1
        
        if (n % 2 == 1):
            result[mid][mid] = filling
            
        return result
```

> [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
>
> 好难 没做出来 可能需要俩offset来记录















