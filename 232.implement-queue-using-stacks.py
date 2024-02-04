#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x: int): # -> None:
        self.stack_in.append(x)

    def pop(self): # -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(self.stack_in):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self): # -> int:
        ans = self.stack_out.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self): # -> bool:
        return not (self.stack_in or self.stack_out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

