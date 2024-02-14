# @before-stub-for-debug-begin
from python3problem150 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from operator import add, sub, mul
class Solution:
    def evalRPN(self, tokens: List[str]): # -> int:
        stack = []
        op_map = {"+": add, "-": sub, "*": mul, "/": lambda x, y: int(x / y)}
        for token in tokens:
            if token not in op_map:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op_map[token](op1, op2))
        return stack.pop()
# @lc code=end

