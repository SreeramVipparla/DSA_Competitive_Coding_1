"""
QUESTION-
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""
"""
ANSWER-
"""
class Solution:
   def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, []
    for ss in s:
        if ss.isdigit():
            num = 10*num + int(ss)
        elif ss in ["-", "+"]:
            res += sign*num
            num = 0
            sign = [-1, 1][ss=="+"]
        elif ss == "(":
            stack.append(res)
            stack.append(sign)
            sign, res = 1, 0
        elif ss == ")":
            res += sign*num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + num*sign
"""
SOURCE-LEETCODE
"""